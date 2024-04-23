import os
from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI
from langchain.chains import RetrievalQA
import streamlit as st
os.environ["OPENAI_API_KEY"] = "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"
#persist_directory = 'C:\\Nandika\\openAIproj\\pdfans\\vectors3'
persist_directory = 'C:\\Nandika\\pdf\\vectorscombined'
embedding = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])
llm=OpenAI()
persist_directory = persist_directory
vectordb=Chroma(persist_directory=persist_directory,embedding_function=embedding)
qa_chain = RetrievalQA.from_chain_type(
llm,
retriever=vectordb.as_retriever()
)

def ask_question(question):    
    result = qa_chain({"query": question})
    print("result: ",result["result"])
    return result["result"]

