from flask import Flask, render_template, request, jsonify
from lex_core import get_lex_response

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/ask", methods=["POST"])
def ask():
    user_input = request.get_json().get("query", "")
    response = get_lex_response(user_input)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

