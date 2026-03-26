from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

template1=PromptTemplate(
    template="write a detailed report on {topic}"
)

llm1=ChatOpenAI(model="gpt-4o-mini")

parser1=StrOutputParser()


template2=PromptTemplate(
    template="Provide a 5 liner summary on following text:{text}"
)

llm2=ChatOpenAI(model="gpt-4o-mini")

parser2=StrOutputParser()

chain= template1 | llm1 | parser1 | template2 | llm2 | parser2

result= chain.invoke({
    "topic":"world war"
})

print(result)



