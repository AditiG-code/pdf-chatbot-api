from langchain_community.vectorstores import FAISS

def create_vector_store(chunks,embeddings):

    vector_store=FAISS.from_documents(chunks,embeddings)
    return vector_store

def retrieve_context(question,vector_store):
    retriever=vector_store.as_retriever()

    retrieved_documents=retriever.invoke(question)

    context="\n\n".join(
        doc.page_content for doc in retrieved_documents
    )
    return context
