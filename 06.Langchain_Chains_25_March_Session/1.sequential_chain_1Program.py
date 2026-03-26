from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
load_dotenv()

prompt=PromptTemplate(
    template="Give me 3 interesting facts about the {topic}"
)

llm=ChatOpenAI(model="gpt-4o")

parser=StrOutputParser()

chain = prompt | llm | parser

result=chain.invoke({
    "topic":"climate change"
})

print(result)
