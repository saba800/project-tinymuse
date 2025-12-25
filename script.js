async function api(url, options) {
  const response = await fetch(url, options);
  return response.json();
}

let lastPrompt = null;

document.getElementById("gen").onclick = async () => {
  const q = document.getElementById("q").value;
  const res = await api(`/api/generate?q=${encodeURIComponent(q)}`);

  if (res.ok) {
    lastPrompt = res;
    document.getElementById("result").textContent = res.text;
  } else {
    document.getElementById("result").textContent = "No prompt found.";
  }
};

document.getElementById("copyBtn").onclick = () => {
  if (!lastPrompt) {
    alert("Generate a prompt first.");
    return;
  }
  navigator.clipboard.writeText(lastPrompt.text);
  alert("Copied to clipboard!");
};

document.getElementById("addBtn").onclick = async () => {
  const text = document.getElementById("newPrompt").value.trim();
  if (!text) {
    alert("Prompt text cannot be empty.");
    return;
  }

  const res = await api("/api/add", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ text })
  });

  if (res.ok) {
    alert("Prompt added successfully.");
    document.getElementById("newPrompt").value = "";
  } else {
    alert("Failed to add prompt.");
  }
};

document.getElementById("favBtn").onclick = async () => {
  if (!lastPrompt) {
    alert("Generate a prompt first.");
    return;
  }

  const note = prompt("Optional note for this favorite:");

  const res = await api("/api/favorite", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({
      prompt_id: lastPrompt.id,
      note: note
    })
  });

  if (res.ok) {
    alert("Saved to favorites.");
    location.reload();
  } else {
    alert("Failed to save favorite.");
  }
};

document.getElementById("searchBtn").onclick = async () => {
  const q = document.getElementById("searchInput").value.trim();
  if (!q) return;

  const res = await api(`/api/search?q=${encodeURIComponent(q)}`);
  const container = document.getElementById("searchResults");
  container.innerHTML = "";

  if (res.ok && res.results.length > 0) {
    res.results.forEach(item => {
      const div = document.createElement("div");
      div.className = "border-bottom p-2";
      div.textContent = item.text;
      container.appendChild(div);
    });
  } else {
    container.innerHTML = "<div class='text-muted small'>No results found.</div>";
  }
};
