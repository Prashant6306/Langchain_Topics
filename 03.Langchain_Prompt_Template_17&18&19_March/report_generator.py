
from langchain_openai import ChatOpenAI
import streamlit as st
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(
    model="gpt-4o-mini"
)

st.title("English to Marathi")
query_text=st.text_input("Type a content to translate")
final_query="translate a above text in marathi {}".format(query_text)

if st.button("Translate"):
    if query_text:
        result=llm.invoke(final_query)
        st.write(result.content)
    else:
        st.warning("please submit your question first")

