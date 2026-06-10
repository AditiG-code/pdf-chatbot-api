#this file will contain chat related endpoints
from fastapi import APIRouter
from app.models.request_models import ChatRequest
from app.services.chat_service import generate_answer
from app.services.pdf_loader import loadPdf
from app.services.chunking import create_chunk
from app.services.embeddings import create_embeddings
from app.services.vectorstore import create_vector_store
from fastapi import UploadFile,File
router=APIRouter()
# we need to endpoints ->upload for getting the pdf from the cleint and ask to get the question from the clent

vector_store=None

@router.post('/upload-file')
def upload(file:UploadFile=File(...)):
    global vector_store

    #create file path
    file_path=f"uploads/{file.filename}"

    #save pdf locally
    with open(file_path,'wb') as f:
        f.write(file.file.read())


    #now we have saved uploaded file in our local system
    # now we follow rag pipeline similary
    documents=loadPdf(file_path)
    chunks=create_chunk(documents)
    embedding=create_embeddings()

    vector_store=create_vector_store(chunks,embedding)

    return {
        "message":"Pdf uploaded successfully"
    }
    
@router.post('/ask')
def ask(request:ChatRequest):

    if vector_store is None:
        return {
            "error":"Please upload pdf file"
        }
    answer=generate_answer(
        request.question,vector_store
    )
    return {
        "answer":answer
    }

#//ask endpoint will need vector store ->will need to produce /make vector store after client 
#send the pdf 
#/backend uvicorn app.main:app --reload


    
    
