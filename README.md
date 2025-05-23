# Siddhant Sharma – Personal Website with RAG Chatbot

A simple, mobile-friendly one-page personal website featuring a Retrieval-Augmented Generation (RAG) chatbot trained on my resume. Users can interact with the chatbot to ask questions about my experience, skills, and projects.

---

## 🛠 Tech Stack

- **Frontend**: HTML + CSS (static site)
- **Backend**: FastAPI
- **RAG Agent**: LangChain + FAISS + Groq API
- **Deployment**: Render

---

## 📁 Project Structure

```
personal-site/
├── backend/
│   ├── main.py               # FastAPI app
│   ├── rag_agent.py          # RAG logic with LangChain + Groq
│   ├── resume.txt            # Plain text version of resume
│   ├── requirements.txt
│   └── Procfile              # Render deployment
├── frontend/
│   ├── index.html            # One-page site
│   └── chatbot.js (optional)
├── .env                      # API key (not committed)
├── README.md
```

---

## 🚀 Getting Started (Locally)

### 1. Clone and Install
```bash
git clone https://github.com/yourusername/personal-site.git
cd personal-site/backend
pip install -r requirements.txt
```

### 2. Add your `.env`
```env
GROQ_API_KEY=your-groq-api-key-here
```

### 3. Run Backend
```bash
uvicorn main:app --reload
```

### 4. Open `frontend/index.html`
- Make sure to replace the iframe `src` with your deployed backend URL (or `localhost` during development).

---

## 🌐 Deployment on Render

1. Push code to a GitHub repo
2. Create a **Web Service** on [Render](https://render.com/)
3. Set:
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `uvicorn main:app --host 0.0.0.0 --port $PORT`
   - **Environment Variable**: `GROQ_API_KEY=your-key`
4. Link frontend to Render URL in `iframe` in `index.html`

---

## 💬 Example Questions for Chatbot
- "What are Siddhant's top skills?"
- "Where did Siddhant work before 2023?"
- "Tell me about the RAG agent project."

---

## 📄 Credits
- Built by **Siddhant Sharma**
- [LinkedIn](https://www.linkedin.com/in/sharmasid14/) | [GitHub](https://github.com/s-siddhant)

---

Feel free to fork and customize this for your own portfolio site!
