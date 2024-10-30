import streamlit as st
from langchain_openai.chat_models import ChatOpenAI

st.title("🦜🔗 Quickstart App")

openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")


def generate_response(input_text):
    model = ChatOpenAI(
        temperature=0.7, 
        api_key=openai_api_key
    )
    messages = [
        ["human", "What does the eligibility verification agent (EVA) do?"],
        ["assistant", "EVA automates the process of verifying a patient’s eligibility and benefits information in real-time, eliminating manual data entry errors and reducing claim rejections."],
        ["human", "What does the claims processing agent (CAM) do?"],
        ["assistant", "CAM streamlines the submission and management of claims, improving accuracy, reducing manual intervention, and accelerating reimbursements."],
        ["human", "How does the payment posting agent (PHIL) work?"],
        ["assistant", "PHIL automates the posting of payments to patient accounts, ensuring fast, accurate reconciliation of payments and reducing administrative burden."],
        ["human", "Tell me about Thoughtful AI's Agents."],
        ["assistant", "Thoughtful AI provides a suite of AI-powered automation agents designed to streamline healthcare processes. These include Eligibility Verification (EVA), Claims Processing (CAM), and Payment Posting (PHIL), among others."],
        ["human", "What are the benefits of using Thoughtful AI's agents?"],
        ["assistant", "Using Thoughtful AI's Agents can significantly reduce administrative costs, improve operational efficiency, and reduce errors in critical processes like claims management and payment posting."],
        ["human", input_text]
    ]
    st.info(model.invoke(messages).content)


with st.form("my_form"):
    text = st.text_area(
        "Enter text:",
        "What does the eligibility verification agent (EVA) do?",
    )
    submitted = st.form_submit_button("Submit")
    if not openai_api_key.startswith("sk-"):
        st.warning("Please enter your OpenAI API key!", icon="⚠")
    if submitted and openai_api_key.startswith("sk-"):
        generate_response(text)