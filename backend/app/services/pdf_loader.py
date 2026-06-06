from langchain_community.document_loaders import PyPDFLoader

def loadPdf(sample):
    
    loader=PyPDFLoader(sample)
    # //this if loader.load make all the pages of pdf in list form 
    # list[documents]

    documents=loader.load()

    return documents




