from langchain_huggingface import ChatHuggingFace
from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

def create_rag_chain():
    llm=ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="openai/gpt-oss-20b"
    )

    prompt=PromptTemplate(
        template="""You are a helpful assistant.
        Answer the question from the provided context only.
        If the information is insufficient just say "I don't know ".
        context: {context}
        Question:{question}
        """,
        input_variables=["context","question"]
        

    )
    parser=StrOutputParser()

    chain=prompt|llm|parser

    return chain