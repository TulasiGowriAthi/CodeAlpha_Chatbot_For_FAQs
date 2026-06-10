import streamlit as st
from nlp_engine import load_faqs, get_best_faq_match

# Page layout configuration
st.set_page_config(page_title="NextGen AI FAQ Assistant", page_icon="🤖", layout="wide")

st.title("🤖 NextGen AI FAQ Assistant")
st.write("Ask me anything about modern AI developer tools, workflow automation, or building autonomous agents!")

# 1. Initialize data and conversational state variables inside session state
if "faq_data" not in st.session_state:
    st.session_state.faq_data = load_faqs()

if "messages" not in st.session_state:
    # Seed the conversation with a welcoming intro message from the bot
    st.session_state.messages = [
        {"role": "assistant", "content": "Hi! I'm your tech automation assistant. What can I help you optimize today?"}
    ]

# 2. Render historical messages from the current active session
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 3. Handle active real-time input from the chat user
if user_input := st.chat_input("Type your question here (e.g., How do I run AI locally?)"):
    
    # Display user's question instantly in the chat window
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Calculate matching response using our backend engine
    bot_response = get_best_faq_match(user_input, st.session_state.faq_data)
    
    # Display the automated match response with a neat typing-box effect
    with st.chat_message("assistant"):
        st.markdown(bot_response)
    st.session_state.messages.append({"role": "assistant", "content": bot_response})