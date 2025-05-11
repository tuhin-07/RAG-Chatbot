# 🧠 RAG Chatbot for Customer Support

A Retrieval-Augmented Generation (RAG) chatbot trained exclusively on customer support documents to assist users with accurate, document-backed responses. If a question falls outside the scope of the provided data, the chatbot will respond with **"I don't know."**

---

## 🚀 Features

- ✅ Answers only using provided support documentation.
- ❌ Will not hallucinate or fabricate answers from outside knowledge.
- 📁 Uses FAISS for fast vector-based retrieval.
- 🤖 Integrates with OpenAI (or other LLMs) for contextual response generation.
- 💬 User-friendly web interface via Streamlit.
- 📦 Self-contained backend with FastAPI.

---

## 🏗️ Project Structure

rag-chatbot/
├── backend/
│ ├── ingest_docs.py # Embedding and indexing of support documents
│ ├── rag_pipeline.py # Retrieval and response generation
│ ├── main.py # FastAPI server to handle chat requests
├── frontend/
│ └── app.py # Streamlit web UI for the chatbot
├── data/
│ └── customer_support_docs/ # Raw support documents (PDF, TXT, etc.)
├── requirements.txt # Python dependencies
├── README.md # You're reading it!



---

## 📦 Requirements

- Python 3.8+
- OpenAI API key (if using OpenAI)
- Recommended: Virtual environment

---

## 🔧 Installation & Setup

### 1. Clone the Repository


```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot

```
### 2. Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
### 3. Install Dependencies
```bash
pip install -r requirements.txt

```

Step-by-Step Usage
✅ Step 1: Add Your Documents
Place all your customer support files (.txt, .pdf, etc.) inside:

data/customer_support_docs/

✅ Step 2: Generate Embeddings & Index
```bash
python backend/ingest_docs.py

This will:

Load and chunk the documents.

Generate embeddings using SentenceTransformer.

Create and save a FAISS index.

Save document chunks in docs.pkl.


```

✅ Step 3: Run the FastAPI Backend

uvicorn backend.main:app --reload
API will run at: http://127.0.0.1:8000/chat

🧠 How It Works
User sends a query via the frontend.

Query is embedded using the same model as used during ingestion.

FAISS index is searched for top similar document chunks.

If similarity is below threshold, respond: "I don't know."

Else, retrieved context is passed to the LLM (e.g., OpenAI GPT) to generate a grounded response.

💬 Running the Web Interface (Streamlit)
In a new terminal:

```bash
streamlit run frontend/app.py
Visit: http://localhost:8501 to chat with your support bot.


⚙️ Configuration
backend/rag_pipeline.py: Customize the number of top results, similarity threshold, and model used.

.env: (Optional) Store OpenAI API key or other settings.

📁 Requirements File (requirements.txt)
txt
Copy
Edit
faiss-cpu
sentence-transformers
openai
fastapi
uvicorn
streamlit


📤 Deployment Options
🔵 Backend: Host on Render, AWS EC2, or Heroku

🟢 Frontend: Deploy via Streamlit Cloud or embed in your site using iframe

🛡️ Limitations
Can only answer based on provided documents

Responses depend on the quality and structure of ingested data

"I don't know" logic depends on a similarity threshold—may require tuning

🧠 Future Enhancements
Add document upload support via web UI

Add feedback/rating system for responses

Explore lightweight open-source LLMs for self-hosting


