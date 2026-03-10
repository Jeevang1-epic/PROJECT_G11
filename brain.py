import os
from dotenv import load_dotenv
from langchain_ollama import ChatOllama
from langchain_linkup import LinkupSearchTool
from langgraph.prebuilt import create_react_agent
from tools import manage_file, open_app, capture_screen

load_dotenv()

# 1. Setup Brain (Ollama)
llm = ChatOllama(
    model="qwen2.5-coder:7b", 
    temperature=0,
    timeout=120
)

# 2. Initialize Tools
search_tool = LinkupSearchTool(depth="deep", output_type="sourcedAnswer")
tools = [search_tool, manage_file, open_app, capture_screen]

agent_executor = create_react_agent(llm, tools)

def run_mission():
    print("\n--- G11: Phase 2 Active (Execution Mode) ---")
    print(f"Deadline: Feb 11, 11:59 PM | User: G1")
    
    while True:
        query = input("\nG11 is listening. What's the mission? (type 'exit' to quit) >> ")
        if query.lower() == 'exit':
            break
            
        inputs = {"messages": [("user", query)]}
        
        try:
            # Stream events to see reasoning and tool calls in real-time
            for event in agent_executor.stream(inputs, stream_mode="values"):
                message = event["messages"][-1]
                
                # Check if it's a Tool Call or a Final Response
                if message.content:
                    print(f"\n[G11]: {message.content}")
                elif hasattr(message, "tool_calls") and message.tool_calls:
                    for tc in message.tool_calls:
                        print(f" [Action]: Calling {tc['name']} with {tc['args']}")

        except Exception as e:
            print(f"\n[System Error]: {e}")

if __name__ == "__main__":

    run_mission()
