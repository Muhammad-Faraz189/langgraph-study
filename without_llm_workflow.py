from langgraph.graph import StateGraph,START,END
# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
from typing import TypedDict
# import os
# load_dotenv()

# gemini_api_key = os.getenv("GOOGLE_API_KEY")

# llm = ChatGoogleGenerativeAI(
#     model = "gemini-3.1-flash-lite-preview",
#     api_key = gemini_api_key
# )



#First step to create state
class BMIState(TypedDict):
    weight_kg : float
    height_m : float
    bmi : float

#Define your graph
graph = StateGraph(BMIState)    

#2nd step to create node
def cal_bmi(state:BMIState) ->BMIState:
    weight =state["weight_kg"]
    height = state["height_m"]
    
    bmi = weight/(height**2)
    state['bmi'] = round(bmi,2)
    return state  

#add node to your graph
graph.add_node("cal_bmi",cal_bmi)

#add edges to your graph
graph.add_edge(START,'cal_bmi')
graph.add_edge('cal_bmi',END)

#compile the graph
workflow = graph.compile()

#invoke
initial_workflow = {"weight_kg" : 60.5, "height_m" : 5.4}

final_workflow = workflow.invoke(initial_workflow)
print(final_workflow)
