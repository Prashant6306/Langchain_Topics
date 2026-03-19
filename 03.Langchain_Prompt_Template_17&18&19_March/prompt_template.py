from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import streamlit as st
load_dotenv()


st.title("AI Content Generator")
# Define a new prompt template
instruction_text = """
Generate a concise explanation for the topic "{topic_name}"

Details:
- Presentation style: {format_style}
- Depth level: {detail_level}

Instructions:
1. Include formulas or technical expressions if applicable
2. Use small code examples where helpful
3. Explain using simple real-life comparisons
4. If data is missing, mention "Details unavailable"
5. Keep the explanation aligned with the requested style and depth
"""

# Create template
template_engine = PromptTemplate(
    template=instruction_text
    )

topic_name=st.text_input("Enter the topic name: ")
format_style=st.text_input("Enter the format style: ")
detail_level=st.text_input("Enter the detailed level or not: ")


prepared_prompt = template_engine.invoke({
    "topic_name": topic_name,
    "format_style": format_style,
    "detail_level": detail_level
})

# Populate template
# prepared_prompt = template_engine.invoke({
#     "topic_name": "Neural Networks Basics",
#     "format_style": "beginner-friendly",
#     "detail_level": "brief"
# })

final_query = prepared_prompt.text

# Initialize model
chat_model = ChatOpenAI(model="gpt-4o-mini")

# Invoke model
#output = chat_model.invoke(final_query)


if st.button("Generate"):
    if final_query:
        result=chat_model.invoke(final_query)
        st.write(result.content)
    else:
        st.warning("please submit your question first")

# print(output.content)