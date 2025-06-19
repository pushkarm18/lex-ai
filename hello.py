from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "🧠 Lex AI is online and working!"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message", "")
    if user_input:
        return jsonify({"response": f"Lex says: You said '{user_input}'"})
    return jsonify({"response": "No message received."})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)

