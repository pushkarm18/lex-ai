const chatbox = document.getElementById("chatbox");
const input = document.getElementById("input");

function sendMessage() {
  const message = input.value.trim();
  if (!message) return;

  appendMessage("You", message);
  input.value = "";

  fetch("/chat", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ message })
  })
  .then(res => res.json())
  .then(data => {
    appendMessage("Lex", data.response);
  })
  .catch(err => {
    appendMessage("Lex", "❌ Error reaching Lex.");
  });
}

function appendMessage(sender, text) {
  const msg = document.createElement("div");
  msg.innerHTML = `<b>${sender}:</b> ${text}`;
  chatbox.appendChild(msg);
  chatbox.scrollTop = chatbox.scrollHeight;
}

function toggleTheme() {
  document.body.classList.toggle("light-mode");
}

