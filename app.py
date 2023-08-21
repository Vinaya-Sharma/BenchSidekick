import streamlit as st
from dotenv import load_dotenv 
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from html_template import css, bot_template, user_template
import os
import gdown
from PyPDF2 import PdfReader


def get_pdf_text(pdf_docs):
    raw_text = ""

    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            raw_text += page.extract_text()

    return raw_text


def get_pdf_text2(link):

    all_text = ""
    # Choose the subdirectory name within the root directory
    subdirectory_name = "Google_Drive_Downloads"

    # Create the subdirectory if it doesn't exist
    target_directory = os.path.join(os.getcwd(), subdirectory_name)
    if not os.path.exists(target_directory):
        os.mkdir(target_directory)

    os.chdir(target_directory)
    print(os.getcwd())

    # Download the Google Drive folder
    gdown.download_folder(link, quiet=True, use_cookies=False)

    # Function to extract text from PDF files
    def get_pdf_text_with_link(pdf_path):
        raw_text = ""
        pdf_reader = PdfReader(pdf_path)
        for page in pdf_reader.pages:
            raw_text += page.extract_text()
        return raw_text

    # Loop through each folder and each file within the directory
    for root, dirs, files in os.walk("."):
        for file in files:
            pdf_path = os.path.join(root, file)
            pdf_text = get_pdf_text_with_link(pdf_path)
            all_text += pdf_text
            os.remove(pdf_path)
        
    for root, dirs, files in os.walk("."):
        for dirr in dirs:
            print(dirr)
            os.rmdir(dirr)
            
    print(os.getcwd())
    os.chdir("..")
    print(os.getcwd())
    os.rmdir(subdirectory_name)
    return all_text


def get_text_checks(raw_text):
    textSplitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
    )
    chunks = textSplitter.split_text(raw_text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vector_store

def get_conversation_chain(vector_store):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(llm=llm, 
                                                               retriever=vector_store.as_retriever(), 
                                                               memory=memory)
    return conversation_chain

def handle_user_question(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']

    for i, message in enumerate(st.session_state.chat_history):
        if i%2 == 0:
            st.write(user_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)
        else:
            st.write(bot_template.replace("{{MSG}}", message.content), unsafe_allow_html=True)



def main():
    load_dotenv()
    st.set_page_config(page_title="benchsidekick", page_icon=":superhero:")
    st.write(css, unsafe_allow_html=True)

    # Add a wrapper div for the fixed header and input field
    st.write('<div class="fixed-header">', unsafe_allow_html=True)
    st.header("benchsidekick! :superhero:")

    if "conversation" not in st.session_state:
        st.session_state.conversation = None

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.text("connect to Drive!")
    pdf_docs = st.text_input("enter drive link: ")

    if st.button("upload"):
        with st.spinner("Uploading your documents..."):
            #get pdf text
            raw_text = get_pdf_text2(pdf_docs)

            #get text chunks 
            text_chunks = get_text_checks(raw_text)
            
            #create vector store 
            vector_store = get_vector_store(text_chunks)

            #create conversation chain 
            st.session_state.conversation = get_conversation_chain(vector_store)

    st.write('<hr/>', unsafe_allow_html=True)

    user_question = st.text_input("ask a question about your documents: ")
    if user_question:
        handle_user_question(user_question)

if __name__=="__main__":
    main()