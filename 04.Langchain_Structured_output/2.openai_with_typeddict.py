from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

feedback_input = """The device performance is solid, but the user interface feels cluttered.
There are several built-in applications that cannot be uninstalled.
Additionally, the design seems a bit old-fashioned compared to competitors.
Expecting improvements in future updates."""

response = model.invoke(feedback_input)

print(response)
print(type(response))

# If you want only text content:
print(response.content)