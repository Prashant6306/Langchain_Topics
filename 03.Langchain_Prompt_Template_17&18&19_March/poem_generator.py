from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()


llm=ChatOpenAI(
    model="gpt-4o"
)

tmpl = "Write a poem about {subject} in a {mood} tone with {lines} lines"

prompt_obj=PromptTemplate(
    template=tmpl
)

subject=input("Enter Subject:")

mood=input("Enter mood of poem to generate:")

lines=int(input("Enter lines of poem to create:"))

complete_prompt=prompt_obj.invoke(
    {
        "subject":subject,
        "mood":mood,
        "lines":lines
    }
)

prompt=complete_prompt.text

result=llm.invoke(prompt)

print(result.content)
