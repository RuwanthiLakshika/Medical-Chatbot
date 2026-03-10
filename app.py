from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import Pinecone as PineconeVectorStore
from langchain_cohere import ChatCohere
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get('PINECONE_API_KEY')
COHERE_API_KEY = os.environ.get('COHERE_API_KEY')

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY
os.environ["COHERE_API_KEY"] = COHERE_API_KEY

embeddings = download_hugging_face_embeddings()

index_name = "medibot"

dosearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

retriever = dosearch.as_retriever(search_type="similarity", search_kwargs={"k":3})

llm = ChatCohere(model="command-r-plus-08-2024", temperature=0)

# Function to format retrieved documents into context text
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

promt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        ("human", "Context:\n{context}\n\nQuestion: {input}"),
    ]
)

# Create a RAG chain that properly formats context
rag_chain = (
    {
        "context": lambda x: format_docs(retriever.invoke(x["input"])),
        "input": lambda x: x["input"]
    }
    | promt
    | llm
    | StrOutputParser()
)

@app.route("/")
def index():
    return render_template('chat.html')

@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain.invoke({"input" : msg})
    print("response :", response)
    return str(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)