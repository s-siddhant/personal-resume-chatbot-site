from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from rag_agent import get_rag_chain
import logging

# Configure logging
logging.basicConfig(
    filename='uvicorn.log',
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

logger = logging.getLogger(__name__)

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize RAG chain
rag_chain = get_rag_chain()

class QueryRequest(BaseModel):
    question: str

@app.post("/api/chat")
async def chat(req: QueryRequest):
    try:
        logger.info(f"Received chat request: {req.question}")
        answer = rag_chain.run(req.question)
        logger.info(f"Generated response for: {req.question}")
        return {"response": answer}
    except Exception as e:
        logger.error(f"Error processing request: {str(e)}")
        raise

# Mount frontend directory AFTER defining API routes
app.mount("/", StaticFiles(directory="../frontend", html=True), name="frontend")