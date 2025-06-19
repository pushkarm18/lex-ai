import tkinter as tk
from lex_core import get_lex_response
import threading
from gtts import gTTS
from playsound import playsound
import uuid
import os

def speak(text):
    filename = f"voice_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    playsound(filename)
    os.remove(filename)

def handle_response():
    user_input = input_field.get()
    if user_input.strip() == "":
        return
    chat_log.config(state=tk.NORMAL)
    chat_log.insert(tk.END, f"You: {user_input}\n")
    input_field.delete(0, tk.END)
    response = get_lex_response(user_input)
    chat_log.insert(tk.END, f"Lex: {response}\n\n")
    chat_log.config(state=tk.DISABLED)
    chat_log.yview(tk.END)
    threading.Thread(target=speak, args=(response,)).start()

# GUI Window
window = tk.Tk()
window.title("Lex - Your AI Assistant")
window.geometry("400x500")
window.configure(bg="#0f172a")

# Chat Log
chat_log = tk.Text(window, state=tk.DISABLED, wrap=tk.WORD, bg="#1e293b", fg="#f8fafc", font=("Segoe UI", 12))
chat_log.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Input + Send
input_frame = tk.Frame(window, bg="#0f172a")
input_field = tk.Entry(input_frame, font=("Segoe UI", 12), width=30)
input_field.pack(side=tk.LEFT, padx=(0, 10), pady=10)
input_field.bind("<Return>", lambda event: handle_response())
send_button = tk.Button(input_frame, text="Send", command=handle_response, bg="#38bdf8", fg="#0f172a", font=("Segoe UI", 12), width=8)
send_button.pack(side=tk.RIGHT)
input_frame.pack(pady=(0, 10))

# ✅ Launch the assistant
window.mainloop()

