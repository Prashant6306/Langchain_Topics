from typing import TypedDict,Annotated,Literal
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

llm=ChatOpenAI(model="gpt-4o-mini")

class ReviewAnalysis(TypedDict):
    summary:Annotated[str,"Provide summary in 1 line not more that that"]
    sentiment:Annotated[Literal["Positive","Negative"],"only in Positive, Negative or Neutral"]

strctured_llm=llm.with_structured_output(ReviewAnalysis)


feedback_input = """The device performance is solid, but the user interface feels cluttered.
There are several built-in applications that cannot be uninstalled.
Additionally, the design seems a bit old-fashioned compared to competitors.
Expecting improvements in future updates."""

result=strctured_llm.invoke(feedback_input)

print(result)