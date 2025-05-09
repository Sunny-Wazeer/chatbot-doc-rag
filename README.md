# chatbot-doc-rag
A document-aware chatbot using LangChain and Retrieval-Augmented Generation (RAG) for answering questions based on custom documents.
# Document-Aware Chatbot using LangChain + RAG

This project is a simple yet powerful **PDF Question-Answering chatbot** built with  and a lightweight Flask web app.

Upload a PDF, ask natural questions about its content, and get context-based answers — all in your browser.

---

## Features

- 🔍 Loads and splits PDF into meaningful text chunks
- 🧠 Uses OpenAI Embeddings (`text-embedding-3-small`)
- 📚 Stores vectors with FAISS for fast similarity search
- 🤖 Answers questions using context retrieved from the PDF only
- 🧼 Simple frontend UI with HTML and JavaScript
- 🌐 Flask backend to connect everything together

---

2. Install Dependencies
Make sure you're using Python 3.9+ and run:
pip install -r requirements.txt

Add Your .env File
Create a .env file in the root folder with your OpenAI key:
OPENAI_API_KEY=your_openai_api_key_here

Usage
1. Place your PDF file
Put your PDF in the project folder (e.g. Colombian_Law_Overview.pdf).

2. Update the file path
Open chatbot.py and update this line if needed:

python
Always show details

Copy
bot = build_pdf_qa_bot("Colombian_Law_Overview.pdf")
3. Run the Flask server
bash
Always show details

Copy
python app.py
4. Open in your browser
Go to:

text
Always show details

Copy
http://127.0.0.1:5000
Now ask questions about your uploaded PDF!

💡 Example
Q: What is the main conclusion of the paper?
A: The chatbot will return the answer based on the PDF content only.

Tech Stack
LangChain

OpenAI API (GPT-3.5 Turbo + Embeddings)

FAISS for vector similarity search

Flask for backend

HTML + JavaScript for frontend

📝 License
This project is licensed under the MIT License — feel free to use and modify.

🙋‍♂️ Author
Made with ❤️ by Sunny Wazeer
Feel free to connect on LinkedIn or Twitter


