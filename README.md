# Guest Support Bot (RAG + Gemini, Bilingual)
A bilingual (English + Arabic) AI-powered guest support chatbot for vacation rental platforms. Built using **FastAPI**, **Gemini LLM**, **FAISS**, and **Streamlit**, this bot can answer guest queries using a static FAQ knowledge base and escalate complex issues to human support.

## Features

- Gemini 1.5 Flash LLM (via Google Generative AI)
- RAG-based response generation with FAISS + Sentence Transformers
- Escalation for queries outside FAQ scope (e.g., "refund", "complaint")
- Streamlit UI for guests
- FastAPI backend with Swagger UI for testing
- English language only (future support for other languages planned)

## Tech Stack
Backend   FastAPI, FAISS, SentenceTransformers 
LLM       Gemini via `google-generativeai` 
Frontend  Streamlit               
Language  English (with planned multilingual support)
Data      Static `faq.json`

## Project Structure

```
├── app
│   ├── api
│   │   ├── chat.py
│   │   ├── embed.py
│   │   └── router.py
│   ├── core
│   │   ├── config.py
│   │   ├── escalation.py
│   │   ├── llm.py
│   │   └── retriever.py
│   ├── data
│   │   └── faq.json
│   ├── embeddings
│   │   └── faiss_index.bin
│   ├── main.py
│   ├── models
│   │   └── schema.py
│   └── services
│       └── embedder.py
├── requirememts.txt
└── ui
│    └── streamlit_app.py
├── README.md
├── .env_example
  ```
## Setup Instructions

### 1. Clone the Repo
```
git clone https://github.com/HafizMuhammdUsamaSaleem/guest-support-bot.git
cd guest-support-bot
```
### 2. Create `.env` from Template

Copy the example environment file and add your Gemini API key:

```
cp .env_example .env

```
The default embedding model is already set to ```all-MiniLM-L6-v2.```

### 3. Install Dependencies
``` pip install -r requirements.txt ```

## Running the App

### Step 1: Start FastAPI Backend

``` uvicorn app.main:app --reload ```
Visit Swagger UI for testing:

http://localhost:8000/docs

**Important:**

You must run ```/api/embed``` to create embeddings before asking questions.

```POST /api/embed``` → creates FAQ embeddings

```POST /api/ask``` → ask questions (English)

### Step 2: Start Streamlit UI
**In a new terminal tab:**

```streamlit run ui/streamlit_app.py```
Streamlit opens at: http://localhost:8501

- Ask: "What time is check-in?"

- You will get polite, LLM-generated responses.

###  Example Queries
```   
      Question                                   Response (LLM-generated)                               
--------------------------------  ------------------------------------------------------ 
"What is the Wi-Fi password?"     "You’ll find the Wi-Fi password in the welcome guide."                

"I want a refund for my booking"  "🚨 Escalated to support team"  

"Can I pay using crypto wallets?" "Sorry, I couldn't find an answer. Escalating to support."
           
```

## Future Enhancements
- **Dynamic FAQ Upload**  
  Allow admins to upload custom FAQ documents (e.g., `.pdf`, `.docx`, `.md`) via the `/api/embed` endpoint, rather than relying solely on a static `faq.json` file.

- **Manual Language Toggle (Planned)**  
  Add an option in the Streamlit UI for users to manually choose their preferred response language (e.g., English / Arabic), instead of relying only on automatic language detection.

- **Multilingual Embedding Support (Planned)**  
  Integrate multilingual embedding models (e.g., `distiluse-base-multilingual-cased-v1`) to improve handling of questions and FAQs in languages beyond English.

- **Multilingual FAQ Input (Planned)**  
  Enable support for uploading bilingual/multilingual FAQ documents and automatically parsing them for international guests.

- **Session History in UI**  
  Maintain and display the conversation history (past questions and answers) in the Streamlit UI to enhance the chat experience.

- **Admin Interface**  
  Build a lightweight admin panel to manage uploaded FAQs, monitor escalated cases, and configure bot behavior.