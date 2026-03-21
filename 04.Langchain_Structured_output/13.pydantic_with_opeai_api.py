from pydantic import BaseModel,Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini")

class ReviewAnalysis(BaseModel):
    summary:str=Field(description="One liner summary")
    sentiment:str=Field(description="positive,negative or neutral")

structured_llm=llm.with_structured_output(ReviewAnalysis)

review="my iphone 13 is very slow, camera is not good, memory is very limited"

result=structured_llm.invoke(review)

print(result)
print(result.summary)
print(result.sentiment)