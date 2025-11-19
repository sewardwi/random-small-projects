import os
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.document_loaders import PyPDFLoader
from langchain.indexes import VectorstoreIndexCreator
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
import gradio as gr

def qa(input_text): # load document
    #loader = PyPDFLoader('/content/drive/MyDrive/Colab Notebooks/NUHandbook.pdf')
    loader = PyPDFLoader('C:/users/wdsew/nuhandbook.pdf')
    docs = loader.load_and_split()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=60, length_function=len) # split the documents into chunks
    texts = text_splitter.split_documents(docs)
    embeddings = OpenAIEmbeddings() # select which embeddings we want to use
    db = FAISS.from_documents(docs, embeddings) # create the vectorestore to use as the index
    retriever = db.as_retriever(search_type="similarity", search_kwargs={"k": 3}) # expose this index in a retriever interface
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), chain_type="map_reduce”, retriever=retriever, return_source_documents=True) # create a chain to answer questions")
    result = qa({"query": input_text})
    output=f"{result['result']} \n \n source_page :{result['source_documents'][0].metadata.get('page')}\n Source PDF : {result['source_documents'][0].metadata.get('source')}" #format the output
    return output # print the result

iface = gr.Interface(fn=qa, inputs="text", outputs="text")
iface.launch(debug=True, share=True)