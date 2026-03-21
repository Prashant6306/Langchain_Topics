from pydantic import BaseModel,Field
from typing import Optional,Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

class ReviewAnalysis(BaseModel):
    summary:str=Field(
        description="One liner summary of the review",
        min_length=10,
        max_length=30
    )
    sentiment:Literal["Positive","Negative","Neutral"]=Field(
        description="sentiment of the review"
    )
    pros:Optional[list[str]]=Field(
        default=None,
        description="List all pros inside the list"
    )
    cons:Optional[list[str]]=Field(
        default=None,
        description="List all cons inside the list"
    )
    reviewer_name:Optional[str]=Field(
        default=None,
        description="Name of the reviewer if mentioned"
    )
    topic:Literal["mobile","laptop","tabler"]=Field(
        description="This is the topic of the review"
    )

llm=ChatOpenAI(model="gpt-4o-mini")

structured_llm=llm.with_structured_output(ReviewAnalysis)

review="""my name is rajesh,My iphone 13 is very slow, camera is not good, also memory is very limited
but good thing is that user experience is good, display is very nice, 
"""

result=structured_llm.invoke(review)

print(result)