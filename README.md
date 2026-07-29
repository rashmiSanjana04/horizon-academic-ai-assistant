> Horizon Academic AI Assistant 

An AI powered assistant that gives Horizon Campus students instant, accurate answers to questions about academic policies exam rules, late submission procedures, appeals, attendance requirements and more  no need to search through manuals or wait for staff answers. 

> Problem Statement 

Horizon Campus students often need quick answers to academic policy questions. 

What happens if I submit an assignment late? 

How do I appeal a grade or exam result? 

What is the minimum attendance percentage required? 

What are the rules during an exam (e.g., lateness, misconduct)? 

Currently, this information is scattered across PDFs, handbooks, and staff emails, making it slow and difficult for students to find the right answers. Staff spend time manually answering the same common questions over and over again. 

Horizon Academic AI Assistant solves this by providing a conversational agent that instantly retrieves and explains the correct policy, supported by official Horizon Campus documentation. 

> Objectives  

Provide 24/7 access to accurate academic policy information. 

 Ensure that answers are based on official Horizon Campus documents. 

 Reduce the workload of academic and administrative staff. 

 Simplify policy understanding for students. 

 Create a scalable academic support system. 

> Features 

Conversational Q&A — Ask questions naturally and get instant answers. 

RAG-based retrieval — Uses official policy documents to provide accurate responses. 

Academic policy coverage — Supports exams, submissions, appeals, attendance, and regulations. 

Source-based responses — Responses are linked to relevant policy sources. 

Agent-based architecture — Separate agents manage retrieval, reasoning, and responses. 

 Fast access — Quickly find policy information without manual searching. 

 
> Tech Stack (component & Technology)

Language - Python 

Retrieval Pipeline - RAG (Retrieval-Augmented Generation) 

LLM - (specify: e.g., OpenAI GPT-4o-mini / Claude / Gemini / local model) 

Vector Store -(specify: e.g., ChromaDB / FAISS) 

Agent Framework - (specify: e.g., LangChain / LlamaIndex / custom) 

Environment Management - Python (venv) 

Version Control - Git and GitHub 

> project Structure

horizon-academic-ai-assistant/
│
├── agents/           Agent modules (query understanding, routing, response generation)
├── rag/              RAG pipeline (retriever, embeddings, vector store logic)
├── data/             Knowledge base — academic policy documents (exam rules, appeals, attendance, etc.)
├── docs/             Project documentation (proposal, diagrams, reports)
├── utils/            Helper/utility functions
│
├── venv/             Python virtual environment (not tracked in Git)
├── README.md         Project overview and setup guide
├── requirements.txt  Python dependencies
└── .gitignore        Files/folders excluded from version control

> Setup Instructions
1. Clone the repo
git clone https://github.com/rashmiSanjana04/horizon-academic-ai-assistant.git
cd horizon-academic-ai-assistant

2. Create & activate a virtual environment
python -m venv venv
.\venv\Scripts\activate      # Windows
source venv/bin/activate     # macOS/Linux

3. Install dependencies
pip install -r requirements.txt

4. Setup environment variables
Create a .env file in the project root (.env.example) and add your API key(s):

5. run the application
python main.py

 > User Flowe 

Student Question
      │
      ▼
[ Retrieval Agent ] ──► Searches Policy Knowledge Base (RAG)
      │
      ▼
[ Response Agent ] ──► Generates Clear Answer
      │
      ▼
Answer + Source Reference
      │
      ▼
   Student

> Future Improvements
Add multi-language support (Sinhala/English)


Developed as part of an academic assignment for Horizon