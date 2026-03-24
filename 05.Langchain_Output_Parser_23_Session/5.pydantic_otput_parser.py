from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from typing import Literal
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel,Field

class ReviewAnalysis(BaseModel):
    summary:str=Field(description="Short summary",max_length=50,min_length=20)
    sentiment:Literal["Positive","Negative","Neutral"]=Field(description="Sentiment of the review")

parser=PydanticOutputParser(pydantic_object=ReviewAnalysis)

template=PromptTemplate(
    template="Above is the review:{review} \n {format_instructions}",
    partial_variables={"format_instructions":parser.get_format_instructions()}
)

review="my iphone 13 is very fast, camera is not good, memory is very limited"

prompt=template.invoke({
    "review":review
})

review="my iphone 13 is very slow, camera is not good, memory is very limited"

llm=ChatOpenAI(model="gpt-4o-mini")

result=llm.invoke(prompt)

final_result=parser.invoke(result)

print(final_result)