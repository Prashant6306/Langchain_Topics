from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

prompt_tpl = PromptTemplate(
    template="Summarise {title} in {style}"
)
# All vars provided — works perfectly
result = prompt_tpl.invoke({
    "title": "BERT Paper"
    #"length":"short" ,# Extra variable
    #"style": "simple" #missing variable
})
print(result.text)
# ✅ StringPromptValue: "Summarise BERT Paper in simple"