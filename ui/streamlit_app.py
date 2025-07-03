import streamlit as st
import requests

st.set_page_config(page_title="AI Concierge", page_icon="🤖", layout="centered")

st.title("🏡 Guest Support Concierge Bot")
st.caption("Ask me anything about your stay: check-in, Wi-Fi, house rules, and more!")

# Input
question = st.text_input("💬 Ask your question:", placeholder="e.g., What time is check-in?")

# Submit
if st.button("Get Answer") and question.strip():
    with st.spinner("Thinking..."):
        try:
            response = requests.post(
                "http://localhost:8000/api/ask",
                json={"question": question}
            )
            if response.status_code == 200:
                answer = response.json()["response"]
                if "escalate" in answer.lower():
                    st.warning(f"🚨 {answer}")
                else:
                    st.success(f"🤖 {answer}")
            else:
                st.error("❌ Failed to get a response from the backend.")
        except Exception as e:
            st.error(f"⚠️ Error: {str(e)}")
