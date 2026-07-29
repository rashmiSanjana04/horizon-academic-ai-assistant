"""
app.py

Streamlit web interface for the Horizon Academic AI Assistant.
Wraps the existing RouterAgent, RetrievalAgent, and ResponseAgent
in a chat UI, deployable to Streamlit Community Cloud.
"""

import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from agents.router_agent import RouterAgent
from agents.retrieval_agent import RetrievalAgent
from agents.response_agent import ResponseAgent

st.set_page_config(page_title="Horizon Academic AI Assistant", page_icon="🎓")

st.title("🎓 Horizon Academic AI Assistant")
st.caption("Ask about exam rules, late submissions, appeals, or attendance.")


@st.cache_resource
def load_agents():
    """Load agents once and cache them across reruns."""
    router = RouterAgent()
    retrieval = RetrievalAgent(top_k=4)
    response = ResponseAgent()
    return router, retrieval, response


router_agent, retrieval_agent, response_agent = load_agents()

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

question = st.chat_input("Ask a question about academic policy...")

if question:
    st.session_state.messages.append({"role": "user", "content": question})
    with st.chat_message("user"):
        st.markdown(question)

    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            category = router_agent.route(question)
            message = retrieval_agent.send_message(question)
            answer = response_agent.receive_message(message)

            st.caption(f"Category: `{category}`")
            st.markdown(answer)

    st.session_state.messages.append({"role": "assistant", "content": answer})