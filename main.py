import os
import subprocess
import tkinter as tk
from tkinter import scrolledtext, messagebox
import requests
from dotenv import load_dotenv
import pickle
import face_recognition

# Load API key from .env
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
MODEL = "llama3-8b-8192"  # Confirm this model is supported

# Validate face data
def is_face_data_present():
    return os.path.exists("face_data/encodings.pkl") and os.path.exists("face_data/user.jpg")

def generate_ai_response(prompt):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "temperature": 0.7
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            return response.json()["choices"][0]["message"]["content"]
        else:
            return f"[Groq Error]: {response.status_code} - {response.json()}"
    except Exception as e:
        return f"[Exception] {e}"

def execute_command():
    user_input = command_entry.get()
    command_entry.delete(0, tk.END)

    output_text.insert(tk.END, f"You: {user_input}\n")

    if user_input.startswith("cd "):
        try:
            os.chdir(user_input[3:].strip())
            output_text.insert(tk.END, f"Changed directory to {os.getcwd()}\n\n")
        except Exception as e:
            output_text.insert(tk.END, f"[cd Error]: {e}\n\n")
    elif user_input.startswith("!"):  # System command
        try:
            result = subprocess.run(user_input[1:], shell=True, capture_output=True, text=True)
            output_text.insert(tk.END, f"{result.stdout or result.stderr}\n")
        except Exception as e:
            output_text.insert(tk.END, f"[Command Error]: {e}\n")
    else:  # AI Prompt
        response = generate_ai_response(user_input)
        output_text.insert(tk.END, f"Assistant: {response}\n\n")

    output_text.see(tk.END)

def start_gui():
    if not is_face_data_present():
        messagebox.showerror("Face Recognition", "Face data not found. Run setup_face.py first.")
        return

    root = tk.Tk()
    root.title("PromptShell")

    # Command input
    global command_entry
    command_entry = tk.Entry(root, width=80, font=("Arial", 12))
    command_entry.pack(padx=10, pady=10)
    command_entry.bind("<Return>", lambda event: execute_command())

    # Output area
    global output_text
    output_text = scrolledtext.ScrolledText(root, width=100, height=30, wrap=tk.WORD, font=("Courier", 10))
    output_text.pack(padx=10, pady=10)

    # Run button
    run_btn = tk.Button(root, text="Run", command=execute_command)
    run_btn.pack(pady=5)

    root.mainloop()

if __name__ == "__main__":
    start_gui()
