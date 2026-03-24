from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini")

template1=PromptTemplate(
    template="write a detailed report on {topic}"
)

prompt1=template1.invoke(
    {
        "topic":"climate change in the world"
    }
)

result1=llm.invoke(prompt1)

parser1=StrOutputParser()

result2=parser1.invoke(result1)

print("=======>",result2)
template2=PromptTemplate(
    template="Provide a 5 liner summary on following text:{text}"
)

prompt2=template2.invoke(
    {
        "text":result2
    }
)

result3=llm.invoke(prompt2)

parser2=StrOutputParser()

result4=parser2.invoke(result3)

print("=======>",result4)






