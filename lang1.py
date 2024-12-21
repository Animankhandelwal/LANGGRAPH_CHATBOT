# Import necessary libraries
import os
from langgraph.graph import StateGraph, START, END
from typing_extensions import TypedDict
from tavily import TavilyClient

# Initialize Tavily client
client = TavilyClient(api_key=os.environ.get("TAVILY_API_KEY"))  # Ensure the environment variable is set

# Define the overall state of the graph (shared across nodes)
class OverallState(TypedDict):
    type: str
    price_range: str
    features: str
    brand: str
    fuel_type: str

# Output from specific nodes can include private data
class NodeOutput(TypedDict):
    private_data: str

# Node 1: Start the conversation
def start_conversation(state: OverallState) -> NodeOutput:
    print("Welcome to the Car Recommendation Chatbot! Let's find the perfect car for you.")
    return {"private_data": "Conversation started"}

# Node 2: Ask for car type
def ask_car_type(state: NodeOutput) -> OverallState:
    car_type = input("What type of car are you looking for? (e.g., SUV, Sedan, Hatchback): ")
    return {"type": car_type, "price_range": "", "features": "", "brand": "", "fuel_type": ""}

# Node 3: Ask for price range
def ask_price_range(state: OverallState) -> OverallState:
    price_range = input("What's your budget range? (e.g., 10000-20000): ")
    state["price_range"] = price_range
    return state

# Node 4: Ask for features
def ask_features(state: OverallState) -> OverallState:
    features = input("What features do you prefer? (e.g., sunroof, GPS, Bluetooth): ")
    state["features"] = features
    return state

# Node 5: Ask for brand
def ask_brand(state: OverallState) -> OverallState:
    brand = input("Do you have a preferred brand?: ")
    state["brand"] = brand
    return state

# Node 6: Ask for fuel type
def ask_fuel_type(state: OverallState) -> OverallState:
    fuel_type = input("What fuel type do you prefer? (e.g., Petrol, Diesel, Electric): ")
    state["fuel_type"] = fuel_type
    return state

# Node 7: Provide recommendations
def provide_recommendation(state: OverallState) -> OverallState:
    # Construct the search query based on user preferences
    query = f"{state['type']} cars under {state['price_range']} with {state['features']} from {state['brand']} running on {state['fuel_type']}"

    try:
        # Perform the search using Tavily's search method
        response = client.search(query, max_results=5)
        results = response.get("results", [])

        if results:
            print("Recommended Cars:")
            for result in results:
                print(f"- {result['title']}: {result['url']}")
        else:
            print("No car recommendations found based on your preferences.")
    except Exception as e:
        print(f"There was an error fetching car recommendations: {e}")
    return state

# Node 8: End the conversation
def end_conversation(state: OverallState) -> None:
    print("Thank you for using the Car Recommendation Chatbot. Have a great day!")

# Build the state graph
builder = StateGraph(OverallState)
builder.add_node(start_conversation)
builder.add_node(ask_car_type)
builder.add_node(ask_price_range)
builder.add_node(ask_features)
builder.add_node(ask_brand)
builder.add_node(ask_fuel_type)
builder.add_node(provide_recommendation)
builder.add_node(end_conversation)

builder.add_edge(START, "start_conversation")
builder.add_edge("start_conversation", "ask_car_type")
builder.add_edge("ask_car_type", "ask_price_range")
builder.add_edge("ask_price_range", "ask_features")
builder.add_edge("ask_features", "ask_brand")
builder.add_edge("ask_brand", "ask_fuel_type")
builder.add_edge("ask_fuel_type", "provide_recommendation")
builder.add_edge("provide_recommendation", "end_conversation")
builder.add_edge("end_conversation", END)

graph = builder.compile()

# Invoke the graph with the initial state
response = graph.invoke({"type": "", "price_range": "", "features": "", "brand": "", "fuel_type": ""})
print(f"\nOutput of graph invocation: {response}")
