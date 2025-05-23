# Siddhant Sharma – Portfolio Website with Resume Chatbot

A modern, responsive portfolio website featuring a chatbot powered by RAG (Retrieval-Augmented Generation) technology. The chatbot is trained on my resume and can answer questions about my experience, skills, and projects.

---

## 🛠 Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: FastAPI
- **AI/ML**: LangChain, FAISS, OpenAI/Groq API
- **Deployment**: Render

---

## 📁 Project Structure

```
resume-portfolio-website/
├── frontend/
│   ├── index.html           # Main portfolio page
│   ├── styles/
│   │   └── main.css        # Styling
│   ├── js/
│   │   └── chat.js         # Chat functionality
│   └── assets/
│       └── SIDDHANT SHARMA.pdf
├── backend/
│   ├── main.py             # FastAPI application
│   ├── rag_agent.py        # RAG implementation
│   ├── resume.txt          # Training data
│   └── requirements.txt
├── .env                    # API keys (not committed)
└── README.md
```

---

## ✨ Features

- Responsive design that works on desktop and mobile
- Dark theme for better readability
- Interactive project cards with "Read More" functionality
- Real-time chat interface with AI-powered responses
- RAG system for accurate resume-based Q&A

---

## 🚀 Getting Started

### 1. Clone and Install Dependencies
```bash
git clone <repository-url>
cd resume-portfolio-website
pip install -r backend/requirements.txt
```

### 2. Configure Environment
Create a `.env` file in the backend directory:
```env
GROQ_API_KEY=your-groq-api-key
OPENAI_API_KEY=your-openai-api-key
```

### 3. Run the Application
```bash
cd backend
uvicorn main:app --reload
```

### 4. Access the Website
Open `http://localhost:8000` in your browser

---

## 💬 Example Chat Queries
- "What are your main technical skills?"
- "Tell me about your experience with NLP"
- "Describe your time series forecasting project"

---

## 🔐 Security Note
- API keys are stored in `.env` file (not committed to repository)
- CORS is enabled for development
- Frontend assets are served through FastAPI's StaticFiles

---

## 📄 Credits
Built by **Siddhant Sharma**
- [LinkedIn](https://www.linkedin.com/in/sharmasid14/)
- [GitHub](https://github.com/s-siddhant)

---

## 📝 License
This project is licensed under the Apache License 2.0
