# 💻 PromptShell - Your Natural Language Terminal Companion 🚀

Welcome to **PromptShell**, the AI-powered assistant that brings your terminal to life. Run system commands, chat with an AI, and navigate your Linux machine using plain language — all from a sleek desktop GUI!

---

## 🌟 Overview

**PromptShell** is a desktop application that transforms the way you interact with your system. Whether you're a student, developer, or power user, PromptShell helps you manage files, open applications, and get instant answers using cutting-edge AI — **just by typing your request**.

Say goodbye to memorizing long commands and hello to a more human terminal experience!

---

## ✨ Key Features

- 💬 **Natural Language Commands** – No need to remember syntax, just type what you want!
- 🧠 **AI Chat Integration** – Ask questions and get instant answers via open-source LLMs.
- 🗂️ **System Operations** – Create/delete folders, open apps, navigate directories, and more.
- 🧑‍💻 **Face Recognition (Optional)** – Add an extra layer of personalized security.
- 🖥️ **Graphical UI** – Easy-to-use GUI built with Tkinter for a smoother workflow.
- 🔐 **Secure API Handling** – Environment-based secret management with `.env` support.

---

## 🔧 Technologies Used

| Layer        | Tech Stack                      |
|--------------|----------------------------------|
| **Frontend** | Tkinter (Python GUI)             |
| **Backend**  | Python (OS, subprocess, OpenCV)  |
| **AI**       | Groq API (Mixtral LLM)           |
| **Security** | dotenv (env file support)        |
| **Recognition** | OpenCV for face auth          |

---

## 🚀 Getting Started

### 1. Clone the Repository
git clone https://github.com/JnapikaPilli/PromptShell.git
cd PromptShell

2. Create a Virtual Environment
python3 -m venv venv
source venv/bin/activate

3. Install Dependencies
pip install -r requirements.txt

4. Add Your API Key
Create a .env file in the root directory:
GROQ_API_KEY=your_groq_api_key

5. (Optional) Set Up Face Authentication
python setup_face.py

7. Run the Application
python main.py
🧪 Example Commands
You Type	PromptShell Does
open my downloads folder	Opens the Downloads directory
create folder named projects	Creates a folder called "projects"
delete folder named test	Deletes "test" folder
change my pwd to /home/user	Changes working directory
what is the capital of France	Replies with “Paris” via GPT
who are you	Friendly AI chat mode
🤝 Contribution Guidelines
We welcome contributions!

🐛 Report bugs

🌟 Suggest new features

🔀 Submit pull requests

💬 Join discussions

Let’s make PromptShell better together!

📩 Get in Touch
Got questions or ideas? Reach out:

📧 jnapikapilli@gmail.com
🔗 GitHub Profile
