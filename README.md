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

 # horizon-academic-ai-assistant
Agentic AI assistant for answering Horizon Campus academic policy related queries using RAG and multiple AI agents.

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

> Future Improvements
Add multi-language support (Sinhala/English)