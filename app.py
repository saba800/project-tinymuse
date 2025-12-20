from flask import Flask, render_template, request, jsonify, g
import sqlite3, random

DB = "tinymuse.db"
app = Flask(__name__)

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DB)
        db.row_factory = sqlite3.Row
    return db

@app.teardown_appcontext
def close_conn(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def index():
    db = get_db()
    cur = db.execute("SELECT id, text FROM prompts ORDER BY created_at DESC LIMIT 10")
    recent = cur.fetchall()
    favs = db.execute("""
        SELECT f.id as fav_id, p.id as prompt_id, p.text, f.note, f.created_at
        FROM favorites f JOIN prompts p ON f.prompt_id = p.id
        ORDER BY f.created_at DESC LIMIT 8
    """).fetchall()
    return render_template("index.html", recent=recent, favorites=favs)

@app.route("/api/generate")
def generate():
    q = request.args.get("q","").strip()
    db = get_db()
    if q:
        cur = db.execute("SELECT id, text FROM prompts WHERE text LIKE ? ORDER BY RANDOM() LIMIT 1", (f"%{q}%",))
    else:
        cur = db.execute("SELECT id, text FROM prompts ORDER BY RANDOM() LIMIT 1")
    row = cur.fetchone()
    if not row:
        return jsonify({"ok": False, "msg": "هیچ پرومپتی پیدا نشد."})
    text = row["text"]
    # quick tweak: sometimes remix the prompt
    remixes = [
        " — now make it short and cinematic.",
        " — imagine it as a comic panel.",
        " — make it into a 3-line haiku.",
        " — flip the perspective: tell it from the villain's view."
    ]
    if random.random() < 0.45:
        text = text + random.choice(remixes)
    return jsonify({"ok": True, "id": row["id"], "text": text})

@app.route("/api/add", methods=["POST"])
def add_prompt():
    data = request.json or {}
    text = (data.get("text") or "").strip()
    if not text:
        return jsonify({"ok": False, "msg": "متن خالیه."})
    db = get_db()
    cur = db.execute("INSERT INTO prompts (text) VALUES (?)", (text,))
    db.commit()
    pid = cur.lastrowid
    return jsonify({"ok": True, "id": pid, "text": text})

@app.route("/api/favorite", methods=["POST"])
def favorite():
    data = request.json or {}
    pid = data.get("prompt_id")
    note = (data.get("note") or "").strip()
    if not pid:
        return jsonify({"ok": False, "msg": "prompt_id لازمه."})
    db = get_db()
    # allow duplicate favorites but that's fine
    db.execute("INSERT INTO favorites (prompt_id, note) VALUES (?,?)", (pid, note))
    db.commit()
    return jsonify({"ok": True})

@app.route("/api/search")
def search():
    q = request.args.get("q","").strip()
    db = get_db()
    cur = db.execute("SELECT id, text FROM prompts WHERE text LIKE ? ORDER BY created_at DESC LIMIT 30", (f"%{q}%",))
    rows = [{"id": r["id"], "text": r["text"]} for r in cur.fetchall()]
    return jsonify({"ok": True, "results": rows})

if __name__ == "__main__":
    app.run(debug=True)
