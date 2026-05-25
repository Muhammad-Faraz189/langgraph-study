from langgraph.graph import StateGraph,START,END
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict
import os
load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")

llm = ChatGoogleGenerativeAI(
    model = "gemini-3.1-flash-lite-preview",
    api_key = gemini_api_key
)



#First step to create state
class ChatState(TypedDict):
    question: str
    answer: str

#Define your graph
graph = StateGraph(ChatState)    

#2nd step to create node
def chatbot(state: ChatState) -> ChatState:

    user_question = state["question"]

    response = llm.invoke(user_question)

    state["answer"] = response.content

    return state 

#add node to your graph
graph.add_node("chatbot",chatbot)

#add edges to your graph
graph.add_edge(START,'chatbot')
graph.add_edge('chatbot',END)

#compile the graph
workflow = graph.compile()

#invoke
initial_workflow = {"question": "what is the benefits of langgraph"}

final_workflow = workflow.invoke(initial_workflow)
print(final_workflow["answer"])
