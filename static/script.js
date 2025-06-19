const input = document.getElementById("userInput");
const chatBox = document.getElementById("chatBox");

function sendMessage() {
  const msg = input.value.trim();
  if (!msg) return;

  chatBox.innerHTML += `<div><b>You:</b> ${msg}</div>`;
  input.value = "";

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message: msg })
  })
  .then(res => res.json())
  .then(data => {
    chatBox.innerHTML += `<div><b>Lex:</b> ${data.response}</div>`;
    chatBox.scrollTop = chatBox.scrollHeight;
  });
}

input.addEventListener("keypress", e => {
  if (e.key === "Enter") sendMessage();
});

// Theme toggle
document.getElementById("modeToggle").addEventListener("change", (e) => {
  document.documentElement.setAttribute("data-theme", e.target.checked ? "light" : "dark");
});
