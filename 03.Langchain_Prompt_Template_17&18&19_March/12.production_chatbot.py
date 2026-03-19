from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

ai_engine   = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)
SYSTEM_ROLE = "You are a knowledgeable and friendly AI assistant"

# Initialise conversation with system persona
dialogue = [SystemMessage(content=SYSTEM_ROLE)]
print(dialogue)
print("Chatbot ready — type 'quit' to exit.\n")

while True:
    user_input = input("You: ").strip()
    if not user_input:
        continue
    if user_input.lower() == "quit":
        print("Goodbye!")
        break

    dialogue.append(HumanMessage(content=user_input))   # ① Log user turn
    print(dialogue)
    response  = ai_engine.invoke(dialogue)               # ② Full context sent
    ai_text   = response.content
    dialogue.append(AIMessage(content=ai_text))          # ③ Log AI reply
    print(dialogue)
    print(f"AI: {ai_text}\n")