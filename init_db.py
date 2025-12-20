import sqlite3

DB = "tinymuse.db"

prompts = [
    "Write a 6-line poem about a robot who learns to dream.",
    "Design a tiny app that helps people remember one small habit.",
    "Imagine a cafe where every table is themed after a different era — describe the menu.",
    "Create a twist ending for a classic myth where the hero becomes the listener.",
    "Sketch a gadget that extracts color from memories."
]

conn = sqlite3.connect(DB)
c = conn.cursor()
c.execute("""CREATE TABLE IF NOT EXISTS prompts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
)""")
c.execute("""CREATE TABLE IF NOT EXISTS favorites (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    prompt_id INTEGER,
    note TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY(prompt_id) REFERENCES prompts(id)
)""")
# insert initial prompts
for p in prompts:
    c.execute("INSERT INTO prompts (text) VALUES (?)", (p,))
conn.commit()
conn.close()
print("DB initialized:", DB)

