from fastapi import FastAPI

import logging

logging.basicConfig(
    level=logging.INFO,
    format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
app = FastAPI(
    title="RAG Chatbot ",
    description="A simple RAG chatbot built with FastAPI",
    version="1.0.0"
)

@app.get("/")
async def root():
    logging.info("Root endpoint called")
    return {"message": "Welcome to the RAG Chatbot API!"}

