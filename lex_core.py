from serpapi import GoogleSearch
import os

SERPAPI_KEY = "4720e02ba3a74c2671ee2e690f5c4196c30d2b2d1308c1de3690fae14ec2d9f3"

import wikipedia

def get_lex_response(user_input):
    # Placeholder logic – customize this!
    if "hello" in user_input.lower():
        return "Hey there! I'm Lex."
    return "I'm still learning, but ask me anything!"

from gtts import gTTS
from playsound import playsound
import os
import uuid

def speak(text):
    filename = f"voice_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def get_lex_response(user_input):
    try:
        if "hello" in user_input.lower():
            return "Hey there! I'm Lex, your assistant."

        elif "who" in user_input.lower() or "what" in user_input.lower():
            try:
                import wikipedia
                summary = wikipedia.summary(user_input, sentences=2)
                return summary
            except:
                pass  # fallback to search

        # Use Google Search
        params = {
            "q": user_input,
            "api_key": SERPAPI_KEY,
            "engine": "google",
            "num": 1
        }

        search = GoogleSearch(params)
        results = search.get_dict()

        answer = ""
        if "answer_box" in results:
            answer = results["answer_box"].get("answer") or results["answer_box"].get("snippet", "")
        elif "organic_results" in results and results["organic_results"]:
            answer = results["organic_results"][0].get("snippet", "Here's what I found.")

        return answer if answer else "Sorry, I couldn't find anything relevant."

    except Exception as e:
        return f"Error fetching answer: {str(e)}"

