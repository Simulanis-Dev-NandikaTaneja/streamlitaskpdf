import warnings
warnings.filterwarnings("ignore")
import os
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

from langchain.vectorstores import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.llms import OpenAI

#from langchain.chat_models import ChatOpenAI
#llm = ChatOpenAI(model_name=llm_name, temperature=0)

from langchain.chains import RetrievalQA
os.environ["OPENAI_API_KEY"] = "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"
llm=OpenAI()
loaders = [
    PyPDFLoader("C:\\Nandika\\try.pdf"),
    PyPDFLoader("C:\\Nandika\\about.pdf"),
    PyPDFLoader("C:\\Nandika\\book.pdf")
]
docs = []
for loader in loaders:
    docs.extend(loader.load())

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 1500,
    chunk_overlap = 150
)

splits = text_splitter.split_documents(docs)

embedding = OpenAIEmbeddings(openai_api_key = os.environ["OPENAI_API_KEY"])

persist_directory = 'C:\\Nandika\\pdf\\vectorscombined'

vectordb = Chroma.from_documents(
    documents=splits,
    embedding=embedding,
    persist_directory=persist_directory
)

print(vectordb._collection.count())


vectordb.persist()
vectordb=None