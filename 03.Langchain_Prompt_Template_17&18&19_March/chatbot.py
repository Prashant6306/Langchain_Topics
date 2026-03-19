from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(
    model="gpt-4o-mini"
)

prompt = st.chat_input("Say something")
if prompt:
    result=llm.invoke(prompt)
    st.write(result.content)


