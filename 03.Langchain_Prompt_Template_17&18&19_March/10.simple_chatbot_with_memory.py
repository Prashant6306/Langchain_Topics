from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

bot= ChatOpenAI()
dialogue_log  = []   # accumulate ALL messages

while True:
    user_text = input("You: ")
    if user_text.lower() == "exit":
        break

    # ① Add user message to history
    dialogue_log.append(user_text)
    print("test1->",dialogue_log)

    # ② Send ENTIRE history to LLM
    reply = bot.invoke(dialogue_log)

    # ③ Store AI response in history
    dialogue_log.append(reply.content)
    print("test1->",dialogue_log)
    print(f"AI: {reply.content}")
