<!DOCTYPE html>
<html>
<head>
    <title>Lex Chat</title>
</head>
<body>
    <h1>Chat with Lex</h1>
    <input id="userInput" type="text" placeholder="Say something...">
    <button onclick="send()">Send</button>
    <div id="chatLog"></div>

    <script>
        async function send() {
            let input = document.getElementById("userInput").value;
            const res = await fetch("/ask", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ message: input })
            });
            const data = await res.json();
            document.getElementById("chatLog").innerHTML += `<p><b>You:</b> ${input}</p><p><b>Lex:</b> ${data.response}</p>`;
        }
    </script>
</body>
</html>
