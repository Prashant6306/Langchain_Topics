from langchain_core.output_parsers import StrOutputParser
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini")

result=llm.invoke("what is the capital of iran?")

print("=======>",result)

parser=StrOutputParser()

final_result=parser.invoke(result)

print("=======>",final_result)