from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from langchain_core.output_parsers import JsonOutputParser

parser=JsonOutputParser()

template=PromptTemplate(
    template="provide a short report on {topic} \n {format_instruction}",
    partial_variables={"format_instruction":parser.get_format_instructions()}
)

llm=ChatOpenAI(model="gpt-4o-mini")

prompt=template.invoke(
    {
        "topic":"cliamte change in world"
    }
)

result=llm.invoke(prompt)

result1=parser.invoke(result)

print(result1)