#generation step
from app.services.vectorstore import retrieve_context,create_vector_store
from app.services.rag_chain import create_rag_chain

def generate_answer(question,vector_store):
    context=retrieve_context(
        question,vector_store
    )
    chain=create_rag_chain()

    answer=chain.invoke({"context":context,"question":question})

    return answer
