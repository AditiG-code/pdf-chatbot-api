#this file will contain chat related endpoints
from fastapi import APIRouter
from app.models.request_models import ChatRequest
from app.services.chat_service import generate_answer
from app.services.pdf_loader import loadPdf
from app.services.chunking import create_chunk
from app.services.embeddings import create_embeddings
from app.services.vectorstore import create_vector_store
from app.services.rag_chain import create_rag_chain

router=APIRouter()

@router.post('/upload')
def upload():

#temporary setup
document=loadPdf("pdfsample.pdf")

chunks=create_chunk(document)

embeddings=create_embeddings()
vector_store=create_vector_store(chunks,embeddings)

@router.post('/ask')
def ask(request:ChatRequest):
    answer=generate_answer(
        request.question,vector_store
    )
    return {
        "answer":answer
    }
    


    
    
