from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

from typing import TypedDict

model=ChatOpenAI(model="gpt-4o-mini",temperature=0)

class Feedbackclass(TypedDict):
    overview:str
    category:str
    emotion:str

structured_model=model.with_structured_output(Feedbackclass)

feedback_input = """The device performance is solid, but the user interface feels cluttered.
There are several built-in applications that cannot be uninstalled.
Additionally, the design seems a bit old-fashioned compared to competitors.
Expecting improvements in future updates."""

result=structured_model.invoke(feedback_input)

print(result)
print(type(result))

# If you want only text content:
# print(result.content)

