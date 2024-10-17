import os
import streamlit as st
from langchain_groq import ChatGroq
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from langchain_community.document_loaders import PyPDFLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings
import google.generativeai as genai
from dotenv import load_dotenv
load_dotenv()
## load the GROQ API Key
os.environ['GROQ_API_KEY']=os.getenv("GROQ_API_KEY")
os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

groq_api_key=os.getenv("GROQ_API_KEY")

llm=ChatGroq(groq_api_key=groq_api_key,model_name="Llama3-8b-8192")
embeddings=GoogleGenerativeAIEmbeddings(model = "models/embedding-001")

st.set_page_config(page_title="Ask your PDF")
st.header("Ask your PDF 📈")

pdf_files=st.file_uploader("Upload a PDF File",type='pdf',accept_multiple_files=True)

prompt=ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate respone based on the question
    <context>
    {context}
    <context>
    Question:{input}

    """

)


def EmbedPDF(dir):
    loader=PyPDFLoader(dir)
    docs=loader.load()
    text_splitter=RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=200)
    final_docs=text_splitter.split_documents(docs)
    vectorsDB=FAISS.from_documents(final_docs,embeddings)
    retriever=vectorsDB.as_retriever()
    return retriever


def QueryPDF(inpt:str,retriever):
    document_chain=create_stuff_documents_chain(llm,prompt)
    retrieval_chain=create_retrieval_chain(retriever,document_chain)
    response=retrieval_chain.invoke({'input':inpt})
    return response['answer']

if pdf_files:
    documents=[]
    for pdf_file in pdf_files:
        temppdf=f"./temp.pdf"
        with open(temppdf,"wb") as file:
            file.write(pdf_file.getvalue())
                        
user_input=st.text_input("Please Enter Your Question!!!")
if pdf_files and user_input is not None:
    db=EmbedPDF(temppdf)
    response=QueryPDF(user_input,db)
    st.write("Answer : ",response)
else:
    st.warning("Please Make sure you have entered your Query and Uploaded Your PDF File!!!!")
    
