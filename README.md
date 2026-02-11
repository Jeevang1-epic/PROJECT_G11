# G11 Desktop Intelligence Agent

G11 is a local desktop assistant built for the **HackWithDC** competition. It utilizes a ReAct framework to execute multi-domain tasks including web search, file management, and system control.

## Project Structure
* **brain.py**: Main execution loop using LangGraph and Ollama.
* **tools.py**: System tools for file I/O, app management, and vision.
* **.env**: Configuration for API keys.

## Core Technology
* **Model**: Qwen 2.5 Coder 7B (via Ollama)
* **Framework**: LangChain and LangGraph
* **Search**: Linkup Agentic Search API
* **Automation**: Python subprocess and pyautogui

## Installation
1. **Install dependencies**: 
   
   pip install -r requirements.txt

## Configure environment: Create a .env file and add your LINKUP_API_KEY.

* **Run the agent**:

python brain.py

## Future Roadmap
* Implementation of vector memory for long-term context.

* Integration of a 3D interface using Three.js.

* Expansion into humanoid robotics control.
