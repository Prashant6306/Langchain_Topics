from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
import streamlit as st

tmpl_str = """
Summarise the research paper titled {paper_title}
with the following requirements:
  - Explanation style  : {style}
  - Summary length     : {length}

Guidelines to follow:
  1. Include relevant mathematical equations if present
  2. Explain concepts using simple, intuitive code snippets
  3. Add relatable analogies to simplify complex ideas
  4. If information unavailable, state 'Insufficient info'
  5. Keep summary clear, accurate, and aligned with the
     requested style and length
"""

prompt_tpl = PromptTemplate(template=tmpl_str)


st.title("Research Paper Assistant")
paper_title=st.text_input("provide paper title: ")
style=st.text_input("provide style:")
length=st.text_input("provide length:")
# Invoke to fill placeholders
filled = prompt_tpl.invoke({
    "paper_title" : "Attention Is All You Need",
    "style"       : "code-oriented",
    "length"      : "medium"
})

prompt=filled.text   # Inspect the filled prompt
llm=ChatOpenAI(
    model="gpt-4o"
)
#result = ai_model.invoke(filled)  # step 2
#st.write(result.content)

if st.button("Generate"):
    if prompt:
        result=llm.invoke(prompt)
        st.write(result.content)
    else:
        st.warning("please submit your question first")