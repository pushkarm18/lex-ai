from flask import Flask, request, jsonify
import os

app = Flask(__name__)

# ✅ Step 1: Load all files from knowledge_base once
knowledge_folder = "knowledge_base"
memory = {}

for filename in os.listdir(knowledge_folder):
    if filename.endswith(".txt"):
        with open(os.path.join(knowledge_folder, filename), 'r', encoding='utf-8') as file:
            memory[filename] = file.read()

# ✅ Step 2: Simple question answering function
def answer_question(question):
    keywords = question.lower().split()

    best_match = ""
    best_score = 0

    for filename, content in memory.items():
        lines = content.splitlines()
        for line in lines:
            score = sum(1 for word in keywords if word in line.lower())
            if score > best_score:
                best_score = score
                best_match = line

    if best_match:
        return best_match
    else:
        return "Sorry, I couldn’t find the answer."

# ✅ Flask route
@app.route('/ask', methods=['POST'])
def ask():
    data = request.get_json()
    question = data.get("question", "")
    answer = answer_question(question)
    return jsonify({"answer": answer})

# ✅ Home page
@app.route("/")
def home():
    return "Lex is ready. Ask questions at /ask using POST."

if __name__ == '__main__':
    app.run(debug=True)

