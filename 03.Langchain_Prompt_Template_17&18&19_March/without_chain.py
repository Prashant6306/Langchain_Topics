from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

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

# step1
filled = prompt_tpl.invoke({
    "paper_title" : "Attention Is All You Need",
    "style"       : "code-oriented",
    "length"      : "medium"
})

print(filled.text)   # Inspect the filled prompt

ai_engine = ChatOpenAI()

#step2
result = ai_engine.invoke(filled)  # step 2
print(result.content)