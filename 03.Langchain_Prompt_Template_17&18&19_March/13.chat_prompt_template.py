# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.messages import SystemMessage, HumanMessage
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()



# # Define multi-turn template with {placeholders}
# chat_tpl = ChatPromptTemplate.from_messages([
#     SystemMessage(
#         content="You are a knowledgeable {domain} expert"
#     ),
#     HumanMessage(
#         content="Explain {concept} in simple terms"
#     ),
# ])

# #Method 1: Fill and inspect
# filled = chat_tpl.invoke({
#     "domain":  "astrophysics",
#     "concept": "black holes",
# })
# prompt=filled.messages

# ai_model = ChatOpenAI(model="gpt-4o-mini")
# response=ai_model.invoke(prompt)

# print(response.content)
# # result=ai_model.invoke(prompt)
# # print(result.content)
# # Method 2: Build chain (recommended)
# # pipeline = chat_tpl | ai_model
# # result   = pipeline.invoke({
# #     "domain":  "astrophysics",
# #     "concept": "black holes",
# # })
# # print(result.content)


from dotenv import load_dotenv
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI

# Load environment variables
load_dotenv()

# Initialize Model
ai_model = ChatOpenAI(model="gpt-4o-mini") # Explicitly naming the model is best practice


chat_tpl = ChatPromptTemplate([
    ("system", "You are a knowledgeable {domain} expert."),
    ("human", "Explain {concept} in simple terms."),
])

# Get user input
domain = input("Enter domain name you like to learn: ")
concept = input("Enter concept you like to learn: ")


filled = chat_tpl.invoke({
    "domain": domain,
    "concept": concept,
})


print("\n--- AI Response ---")
pipeline = chat_tpl | ai_model
result = pipeline.invoke({
    "domain": domain,
    "concept": concept,
})

print(result.content)