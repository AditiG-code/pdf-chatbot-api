import streamlit as st
import requests

# creating UI
st.title("PDF CHATBOT")

pdf_uploaded=st.file_uploader(
    "Upload a file",
    type="pdf"
)
# this line will pdf input option ,in input form
# // this pdf_upload  will use api to send pdf to backend uploaded by user

#call to api
if pdf_uploaded is not None:

    files={
        "file":pdf_uploaded
    }
    
    responce=requests.post(
        "http://127.0.0.1:8000/upload-file",
        files=files
        
    )

    if responce.status_code ==200:
        st.success("PDF Uploaded Successfully")

    st.session_state["uploaded"] = True

# question
if st.session_state.get("uploaded"):
    question=st.text_input("Ask a question from uploaded pdf")
    # this will take question as input from user and then give it to api to call backend


    # make button ->only generate answer when button is clicked
    if st.button("Ask"):

        data = {
            "question": question
        }

        response = requests.post(
            "http://127.0.0.1:8000/ask",
            json=data
        )

        result = response.json()
        if "answer" in result:

            st.write(result["answer"])

        else:

            st.error(result["error"])


# streamlit run app.py