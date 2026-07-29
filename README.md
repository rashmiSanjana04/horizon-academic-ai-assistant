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

> ## Agent-to-Agent Communication

The assistant uses an 'AgentMessage' protocol to enable communication between specialized agents. When a user submits a question, the 'retrieval_agent' searches the knowledge base and sends the relevant policy context to the 'response_agent' using and 'AgentMessage'. The 'response_agent' validates the received message and generates a clear, source-grounded response based on the retrieved information.

### Message Structure (`agents/message.py`)


| sender | Agent sending the message (e.g., 'retrieval_agent') |
| receiver | Agent the message is intended for |
| message_type| Type of message (e.g., `context_found`) used to validate the communication |
| payload | Actual data being passed (user query and |retrieved policy context) |

### Implementation

Student → main.py → RetrievalAgent.send_message()
                          ↓ (AgentMessage: context_found)
                     ResponseAgent.receive_message()
                          ↓
                     Answer → Student

### Example Run

```
You: What happens if I submit my assignment 2 days late?

[response_agent] received message from retrieval_agent:
AgentMessage(
    from=retrieval_agent,
    to=response_agent,
    type=context_found
)

Assistant: According to the **Late Submission Policy**:

* If you submit your assignment between 24 and 48 hours late (up to 2 days), it will be penalized by 20% of the total marks available.
* If you submit more than 48 hours (2 days) after the deadline, your work will not be accepted and will be recorded as a non-submission (0 marks), unless you have been granted an official extension or approved mitigating circumstances.

> Agentic Design Patterns
 1. Tool-Use Pattern (`agents/retrieval_agent.py`)
The RetrievalAgent uses the vector store as a tool to search and retrieve relevant policy documents. This follows the Tool-Use pattern because the agent uses an external knowledge source instead of relying only on the LLM.
2. Router Pattern (`agents/router_agent.py`)
The RouterAgent classifies user questions into categories using keyword matching and directs them to the relevant retrieval process. This helps handle different policy queries efficiently.
3. Reflection / Self-Critique Pattern (`agents/response_agent.py`)
The ResponseAgent uses `reflect_on_answer()` to verify whether the generated answer is supported by retrieved context. It returns GROUNDED or UNGROUNDED to detect unsupported responses.
**Example run showing all three patterns working together:**
```
You: What happens if I submit my assignment 2 days late?
[router_agent] classified question as: late_submission
[response_agent] received message from retrieval_agent: AgentMessage(from=retrieval_agent, to=response_agent, type=context_found)
[response_agent] reflection verdict: GROUNDED
Assistant: According to the Late Submission Policy:
* If you submit your assignment between 24 and 48 hours (up to 2 days) late, your work will be penalized by 20% of the total marks available.
* If you submit more than 48 hours (2 days) after the deadline, your work will not be accepted and will be recorded as a non-submission (0 marks), unless an extension has been granted or an approved mitigating circumstances claim applies.

## Model Selection Strategy

This project uses different AI models for different agent tasks based on latency, cost, and reasoning requirements. The `RouterAgent` uses **Llama 3.1 8B Instant from Groq** because question classification is a simple routing task that requires fast response time and low computational cost. The `ResponseAgent` uses **Gemini Flash Latest from Google** because answer generation requires stronger reasoning capabilities to produce accurate, context-grounded responses using retrieved policy documents.

| Sub-task | Model (Provider) | Why Chosen |
|---|---|---|
| Question classification (routing) | Llama 3.1 8B Instant (Groq) | Low latency and low cost make it suitable for a simple single-word classification task. |
| Answer generation | Gemini Flash Latest (Google) | Provides better reasoning ability to generate accurate responses using retrieved policy information. |
| Reflection / self-critique | Gemini Flash Latest (Google) | Used for verifying answers against retrieved context because it requires stronger reasoning. |

### Implementation
- `agents/router_agent.py` — Uses `ChatGroq(model="llama-3.1-8b-instant")` for question classification.
- `agents/response_agent.py` — Uses `ChatGoogleGenerativeAI(model="gemini-flash-latest")` for answer generation and reflection.

### Known Limitation
The assignment recommends using OpenRouter and/or Groq providers. This project uses Groq for the routing task and Google Gemini directly for answer generation and reflection due to free-tier availability and development constraints.

### ## Live Demo
🔗 [Try the live app](https://horizon-academic-ai-assistant...streamlit.app)








