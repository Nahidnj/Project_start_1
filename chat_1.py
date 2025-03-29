# import openai
# import os


# client = openai.OpenAI(
#     api_key="sk-proj"  # ← کلیدت رو اینجا بذار
# )

# def teaching_assistant_bot(question):
#     response = client.chat.completions.create(
#         model="gpt-3.5-turbo",
#         messages=[
#             {"role": "system", "content": "You are a helpful teaching assistant. Do not give direct answers. Instead, guide students step by step."},
#             {"role": "user", "content": question}
#         ],
#         temperature=0.7,
#         max_tokens=300
#     )
#     return response.choices[0].message.content

# # حالت چت ترمینالی
# while True:
#     user_input = input("👩‍🎓 Student: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("👋 Goodbye!")
#         break
#     reply = teaching_assistant_bot(user_input)
#     print("🤖 Assistant:", reply)

#################################
# import openai

# client = openai.OpenAI(
#     api_key="",
#     base_url="https://openrouter.ai/api/v1"
# )

# # تاریخچه چت اولیه شامل دستورالعمل بات
# messages = [
#     {"role": "system", "content": "You are a helpful teaching assistant. Do NOT give direct answers to the qestion. Instead, ask one question in each step to make the student approach himselt to the answer."}
# ]

# def teaching_assistant_bot(user_input):
#     messages.append({"role": "user", "content": user_input})
#     response = client.chat.completions.create(
#         model="openai/chatgpt-4o-latest",
#         messages=messages,
#         temperature=0.7,
#         max_tokens=300
#     )
#     reply = response.choices[0].message.content
#     messages.append({"role": "assistant", "content": reply})
#     return reply

# # چت در ترمینال
# while True:
#     user_input = input("👩‍🎓 Student: ")
#     if user_input.lower() in ["exit", "quit"]:
#         print("👋 Goodbye!")
#         break
#     try:
#         reply = teaching_assistant_bot(user_input)
#         print("🤖 Assistant:", reply)
#     except Exception as e:
        # print("❌ Error:", e)
##################################

import openai
import streamlit as st
import os


client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY"),  
    base_url="https://openrouter.ai/api/v1"
)


# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are a helpful teaching assistant. Do NOT give direct answers to the qestion. Instead, ask one question in each step to make the student approach himselt to the answer."}
    ]

# UI
st.set_page_config(page_title="Teaching Assistant Bot", page_icon="🏫")
st.title("📘 Teaching Assistant Chatbot")
st.markdown("_Ask your questions and let the bot guide you step-by-step without giving direct answers._")

# Chat display
for msg in st.session_state.messages[1:]:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Ask a question...")
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    with st.spinner("Thinking..."):
        try:
            response = client.chat.completions.create(
                model="deepseek-ai/deepseek-chat",
                messages=st.session_state.messages,
                temperature=0.7,
                max_tokens=300
            )
            reply = response.choices[0].message.content
            st.session_state.messages.append({"role": "assistant", "content": reply})
            with st.chat_message("assistant"):
                st.markdown(reply)
        except Exception as e:
            st.error(f"❌ Error: {e}")
#st.write("API KEY FOUND?" , os.getenv("OPENAI_API_KEY"))

