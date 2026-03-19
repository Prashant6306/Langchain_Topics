from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()

ai_model = ChatOpenAI(model="gpt-4o-mini")

# ① Template with a named slot for injecting saved messages
support_tpl = ChatPromptTemplate([
    SystemMessage(content="You are a friendly customer support agent"),
    MessagesPlaceholder(variable_name="prior_chat"),   # ← history slot
    HumanMessage(content="{new_query}"),               # ← current question
])

# ② Saved messages loaded from database / session store
prior_chat = [
    HumanMessage(content="I need a refund for order #56789"),
    AIMessage(content="Your refund will be processed within 3-5 business days"),
]

# ③ Fill template: inject history + new query
filled = support_tpl.invoke({
    "prior_chat" : prior_chat,
    "new_query"  : "Where is my refund?",
})

# ④ LLM now has FULL context — Day 1 + Day 3 combined
result = ai_model.invoke(filled.messages)
print(result.content)
# → "Based on our earlier conversation, your refund for order #56789 should
#    arrive within the 3–5 business day window we discussed..."