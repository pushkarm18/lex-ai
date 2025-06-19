from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    message = request.json.get("message")
    response = f"Lex says: {message}"  # You can replace with real logic later
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)

