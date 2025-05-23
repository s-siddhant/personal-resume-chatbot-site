from langchain_community.vectorstores import FAISS
from langchain_openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

import os

# Load environment variables from .env file
load_dotenv()

# Set API Keys
groq_api_key = os.getenv("GROQ_API_KEY")
openai_api_key = os.getenv("OPENAI_API_KEY")

# Validate keys
if not groq_api_key or not openai_api_key:
    raise ValueError("Missing required API keys in .env file")

# Set keys in environment
os.environ["OPENAI_API_KEY"] = openai_api_key
os.environ["GROQ_API_KEY"] = groq_api_key

RESUME_PATH = "resume.txt"

def load_documents():
    """Reads and splits resume text into chunks."""
    with open(RESUME_PATH, "r", encoding="utf-8") as file:
        text = file.read()

    splitter = CharacterTextSplitter(chunk_size=900, chunk_overlap=50)
    chunks = splitter.split_text(text)
    return [Document(page_content=chunk) for chunk in chunks]

def get_rag_chain():
    """Creates a RAG chain for QA using FAISS + Groq."""
    if os.path.exists("resume_vectorstore"):
        db = FAISS.load_local(
            "resume_vectorstore", 
            OpenAIEmbeddings(),
            allow_dangerous_deserialization=True
        )
    else:
        docs = load_documents()
        db = FAISS.from_documents(docs, OpenAIEmbeddings())
        # Save for future use
        db.save_local("resume_vectorstore")

    retriever = db.as_retriever()

    llm = ChatOpenAI(
        model="llama3-70b-8192",
        base_url="https://api.groq.com/openai/v1",
        api_key=groq_api_key,
        temperature=0
    )
    rag_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=False
    )
    return rag_chain
