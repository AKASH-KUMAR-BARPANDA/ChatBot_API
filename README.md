# 🧠 FastAPI + Groq Chatbot API

This project is a **chatbot backend** built using **FastAPI** and the **Groq API** (`openai/gpt-oss-20b` model).  
It exposes a simple REST API that accepts user messages and returns chatbot responses powered by Groq’s LLM.

---

## 📂 Folder Structure

ChatBot_API/
│── BASE_PYDANTIC/
│   └── BASEMODEL.py         # Pydantic request models
│
│── GROQ_SERVER/
│   └── GROQ_SERVER_API.py   # Groq API integration
│
│── REPOSITORY/
│   └── CHAT.py              # Bot response logic
│
│── ROUTERS/
│   └── ROUTES.py            # FastAPI routes
│
│── main.py                  # FastAPI entry point
│── requirements.txt         # Dependencies
│── README.md                # Project documentation

---

## ⚙️ Installation

### 1️⃣ Clone the repo
```bash
git clone https://github.com/yourusername/ChatBot_API.git
cd ChatBot_API

2️⃣ Create & activate virtual environment
python -m venv .venv
source .venv/bin/activate   # Mac/Linux
.venv\Scripts\activate      # Windows

3️⃣ Install dependencies
pip install -r requirements.txt

4️⃣ Set your Groq API Key
Open GROQ_SERVER/GROQ_SERVER_API.py and add your key:
client = Groq(api_key="your_api_key_here")

📌 API Usage

▶️ Run the server
uvicorn main:app --reload
The API will be available at:
http://127.0.0.1:8000


📍 Endpoint

POST /chats

Request Body
{
  "Message": "Hello Groq!"
}
Response
{
  "replay": "Hi! How can I help you today?"
}
🛠 Tech Stack
	•	FastAPI → Web framework
	•	Pydantic → Request validation
	•	Groq Python SDK → LLM integration
	•	Uvicorn → ASGI server

⸻

📜 File Descriptions
	•	BASE_PYDANTIC/BASEMODEL.py → Defines request models.
	•	GROQ_SERVER/GROQ_SERVER_API.py → Handles Groq API requests.
	•	REPOSITORY/CHAT.py → Chatbot response logic.
	•	ROUTERS/ROUTES.py → Defines API routes.
	•	main.py → FastAPI entry point.

⸻

🚀 Future Improvements
	•	Add streaming responses (real-time token streaming).
	•	Store conversation history.
	•	Deploy on Render / Railway / AWS Lambda.
	•	Add frontend (React / Next.js) for chat UI.

⸻

📦 Requirements

Here’s a minimal requirements.txt you can use:
fastapi
uvicorn
groq
pydantic

✨ Built with FastAPI & Groq — simple, scalable, and blazing fast!

