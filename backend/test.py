from app.services.pdf_loader import loadPdf
from app.services.chunking import create_chunk
from app.services.embeddings import create_embeddings
from app.services.vectorstore import create_vector_store,retrieve_context
from app.services.rag_chain import create_rag_chain
from app.services.chat_service import generate_answer

# step 1 load pdf

document=loadPdf("/Users/aditigupta/pdf-rag-chatbot/backend/pdfsample.pdf")

#step 2 create chunk
chunks=create_chunk(document)

# step 3 create embeddings
embeddings=create_embeddings()

#step 4 vector store
vector_store=create_vector_store(chunks,embeddings)

#step 5 retriever
question="What are the benefits of automated reasoning?"

# context_retrieve=retrieve_context(question,vector_store)

# step 5 generate answer
final_answer=generate_answer(
    question,vector_store
)

print("\nAnswer\n")
print(final_answer)

