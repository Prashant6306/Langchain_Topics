from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
from langchain_core.prompts import PromptTemplate

from langchain.output_parsers import StructuredOutputParser, ResponseSchema

schema=[
    ResponseSchema(name="fact1",description="fact1 about the topic"),
    ResponseSchema(name="fact2",description="fact2 about the topic"),
    ResponseSchema(name="fact3",description="fact3 about the topic")
]

llm=ChatOpenAI(model="gpt-40-mini")

parser=StructuredOutputParser.from_response_schemas(schema)

template=PromptTemplate(
    template="write a 3 fact about the {topic} \n {format_instruction}",
    partial_variables={
        "format_instruction":parser.get_format_instructions()
    }
)

prompt=template.invoke(
    {
        "topic":"impact of climate change on human"
    }
)

result=llm.invoke(prompt)

final_result=parser.invoke(result)

print(final_result)