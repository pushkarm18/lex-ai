from flask import Flask, request, render_template
import json
import os

app = Flask(__name__)

def load_knowledge():
    if os.path.exists("knowledge.json"):
        with open("knowledge.json", "r") as f:
            return json.load(f)
    return {}

def save_knowledge(knowledge):
    with open("knowledge.json", "w") as f:
        json.dump(knowledge, f, indent=4)

knowledge = load_knowledge()

def lex_reply(user_input):
    user_input = user_input.strip().lower()

    if user_input == "bye":
        return "Goodbye, Pushkar! 👋"

    if user_input.endswith("?"):
        question = user_input.replace("what is", "").replace("?", "").strip()
        return f"{question.capitalize()} is {knowledge.get(question, 'unknown')} 🤔"

    if " is " in user_input:
        key, value = user_input.split(" is ", 1)
        key = key.strip().lower()
        knowledge[key] = value.strip()
        save_knowledge(knowledge)
        return f"Got it! {key.capitalize()} is {value}. 🧠"

    return "Try asking a question or teaching me something using ‘X is Y’. 😊"

@app.route("/", methods=["GET", "POST"])
def home():
    reply = ""
    if request.method == "POST":
        user_input = request.form["message"]
        reply = lex_reply(user_input)
    return render_template("index.html", reply=reply)

if __name__ == "__main__":
    app.run(debug=True)
