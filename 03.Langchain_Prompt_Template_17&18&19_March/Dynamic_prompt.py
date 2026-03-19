from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(
    model="gpt-4o-mini"
)
length=input("provide a length of the report (short/medium/long):")
subject=input("provide a subject on which you want to create a report")

prompt="create a {} report on {}".format(length,subject)
#query="Tell me about AI in 3 short bullet points in numbered list with one sentence each for a 12 year old"
result=llm.invoke(prompt)

print(result.content)
print(result.response_metadata)