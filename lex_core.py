import json
from serpapi import GoogleSearch
import os
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
    if not SERPAPI_KEY or SERPAPI_KEY.strip() == "":
        return "⚠️ Google Search is disabled (API key missing)."
    
    try:
        params = {
            "q": query,
            "api_key": SERPAPI_KEY,
            "engine": "google"
        }
        search = GoogleSearch(params)
        results = search.get_dict()

        return results.get("answer_box", {}).get("answer") or \
               results.get("answer_box", {}).get("snippet") or \
               results.get("organic_results", [{}])[0].get("snippet", "No result found.")
    
    except Exception as e:
        return f"Google Search error: {str(e)}"

def search_wikipedia(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except Exception as e:
        return f"Wikipedia search failed: {str(e)}"

def get_lex_response(msg):
    mem = load_memory()
    msg_lower = msg.lower().strip()

    # Save memory
    if " is " in msg and not msg_lower.startswith("what is"):
        key, val = msg.split(" is ")
        mem[key.strip()] = val.strip()
        save_memory(mem)
        return f"📌 Remembered: {key.strip()} is {val.strip()}"

    # Recall from memory
    elif msg_lower.startswith("what is"):
        key = msg[8:].strip()
        return mem.get(key, search_wikipedia(key))

    # Google Search
    elif msg_lower.startswith("search "):
        return search_google(msg[7:].strip())

    # Wikipedia Search
    elif msg_lower.startswith("wiki "):
        return search_wikipedia(msg[5:].strip())

    # Fallback reply
    return f"🤖 I'm still learning. You said: {msg}"

