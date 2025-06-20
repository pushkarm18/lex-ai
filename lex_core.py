import json, os
from serpapi import GoogleSearch
import wikipedia

MEMORY_FILE = "memory.json"
SERPAPI_KEY = os.getenv("4720e02ba3a74c2671ee2e690f5c4196c30d2b2d1308c1de3690fae14ec2d9f3")

def load_memory():
    try:
        with open(MEMORY_FILE, "r") as f:
            return json.load(f)
    except:
        return {}

def save_memory(mem):
    with open(MEMORY_FILE, "w") as f:
        json.dump(mem, f)

def search_google(query):
    try:
        params = {
            "q": query,
            "api_key": SERPAPI_KEY,
            "engine": "google"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        answer = results.get("answer_box", {}).get("answer") or \
                 results.get("answer_box", {}).get("snippet") or \
                 results.get("organic_results", [{}])[0].get("snippet", "No answer found.")
        return answer
    except Exception as e:
        return f"Google search failed: {str(e)}"

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"Wikipedia search failed: {str(e)}"

def get_lex_response(msg):
    mem = load_memory()
    msg_lower = msg.lower()

    if " is " in msg:
        key, val = msg.split(" is ")
        mem[key.strip()] = val.strip()
        save_memory(mem)
        return f"Remembered: {key.strip()} is {val.strip()}"

    elif msg_lower.startswith("what is"):
        key = msg[8:].strip()
        return mem.get(key, search_wikipedia(key))
    elif msg_lower.startswith("search "):
        return search_google(msg[7:].strip())

    elif msg_lower.startswith("wiki "):
        return search_wikipedia(msg[5:].strip())

    return f"You said: {msg}"


