from typing import TypedDict,Annotated,Literal,Optional
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini")

class ReviewAnalysis(TypedDict):
    Overview:Annotated[str,"provide short overview of review"]
    sentiment:Annotated[Literal["Positive","Negative","Mixed"],"provide sentiment"]
    topic:Annotated[Literal["laptop","mobile","tablet"],"this is the topic of the review"]
    pros:Annotated[Optional[list[str]],"List all pros mentioned"]
    cons:Annotated[Optional[list[str]],"List all cons mentioned"]


structured_llm=llm.with_structured_output(ReviewAnalysis)

feedback_input = """my macbook m4 is very fast, I am very stastified with it's performance,
battry is very good, camera is nice"""

result=structured_llm.invoke(feedback_input)

print(result)