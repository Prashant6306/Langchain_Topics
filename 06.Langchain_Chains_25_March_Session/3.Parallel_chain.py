from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
load_dotenv()

llm=ChatOpenAI(model="gpt-4o")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template="create a short notes on {topic}"
)

prompt2=PromptTemplate(
    template="create 3 quiz questions on {topic}"
)

prompt3=PromptTemplate(
    template="combine the below study material into 1 document: \n Notes: {notes} \n Quiz: {quiz}"
)

parallel_workflow=RunnableParallel(
    {
        "notes":prompt1|llm|parser,
        "quiz":prompt2|llm|parser

    }
)

#merge_chain=prompt3|llm|parser
full_pipeline=parallel_workflow|prompt3|llm|parser

result=full_pipeline.invoke({
    "topic":"map function in python"
})

print(result)