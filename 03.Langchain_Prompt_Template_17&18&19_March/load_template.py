from langchain_core.prompts import load_prompt
import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


loded_tpl=load_prompt("research_template.json")


st.title("Research Paper Assistant")
paper_title=st.text_input("provide paper title: ")
style=st.text_input("provide style:")
length=st.text_input("provide length:")
# Invoke to fill placeholders
filled = loded_tpl.invoke({
    "paper_title" : paper_title,
    "style"       : style,
    "length"      : length
})

prompt=filled.text   # Inspect the filled prompt
llm=ChatOpenAI(
    model="gpt-4o-mini"
)
#result = ai_model.invoke(filled)  # step 2
#st.write(result.content)

if st.button("Generate"):
    if prompt:
        result=llm.invoke(prompt)
        st.write(result.content)
    else:
        st.warning("please submit your question first")

