import os
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Load .env
load_dotenv()

# Step 1: Load PDF
def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    return pages

# Step 2: Split PDF into chunks
def split_docs(docs):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    return splitter.split_documents(docs)

# Step 3: Embed and store in FAISS
def create_vector_store(chunks):
    embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
    return FAISS.from_documents(chunks, embeddings)

# Format retriever results into context
def format_docs(retrieved):
    return "\n\n".join(doc.page_content for doc in retrieved)

# Main function
def build_pdf_qa_bot(pdf_path):
    pages = load_pdf(pdf_path)
    chunks = split_docs(pages)
    vector_store = create_vector_store(chunks)
    retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})

    prompt = PromptTemplate(
        input_variables=["context", "question"],
        template="""
You are an assistant answering questions based on a PDF document.
Only answer based on the provided context.
If you don't know, say "I don't know".

Context:
{context}

Question: {question}
""")

    chain = (
        {
            "context": retriever | RunnableLambda(format_docs),
            "question": RunnablePassthrough()
        }
        | prompt
        | ChatOpenAI(model="gpt-3.5-turbo", temperature=0.2)
        | StrOutputParser()
    )

    return chain

# Example usage
if __name__ == "__main__": # Replace with your PDF path
    bot = build_pdf_qa_bot(r"C:\Users\HP\Desktop\YouTube Transcript Bot\Colombian_Law_Overview.pdf")
    question = "What is the main conclusion of the paper?"
    answer = bot.invoke(question)
    print("Answer:", answer)
