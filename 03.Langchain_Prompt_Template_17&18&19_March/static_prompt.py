from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(
    model="gpt-4o-mini"
)

prompt="create a report on climate change"
#query="Tell me about AI in 3 short bullet points in numbered list with one sentence each for a 12 year old"
result=llm.invoke(prompt)

print(result.content)
print(result.response_metadata)