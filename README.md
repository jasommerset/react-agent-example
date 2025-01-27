# ReAct Framework Example: Logistics Route Planner

A demonstration of building an AI agent using the ReAct (Reasoning and Acting) framework with Google's Gemini LLM. This example shows how to implement ReAct patterns in a practical scenario.

## What is ReAct? 🤔

ReAct is a framework that helps AI agents:
- **Re**ason about what they should do
- Take **Act**ions using available tools
- Observe results and learn from them

The framework follows this pattern:
1. Think about the current state and goal
2. Choose an appropriate action
3. Execute the action using available tools
4. Observe the results
5. Decide what to do next

In this example, we demonstrate these concepts using a logistics scenario where the agent:
- Finds optimal shipping routes
- Checks traffic and weather conditions
- Dispatches trucks and drivers

## Features 🌟

- Complete ReAct implementation showing:
  - Structured thinking and reasoning
  - Tool selection and usage
  - Multi-step planning
  - Result observation and adaptation
- Detailed logging of:
  - Prompts sent to LLM
  - Raw LLM responses
  - Tool executions and results
- Configurable execution delay for readability
- Example tools for logistics:
  - `find_routes`: Discovers shipping routes
  - `check_conditions`: Evaluates conditions
  - `dispatch_truck`: Assigns resources
- Built with Google's Gemini LLM
- Simple command-line interface

## Quick Start 🚀

1. Clone this repository:
```bash
git clone https://github.com/jasommerset/react-agent-example.git
cd react-agent-example
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up your Google API key:
```bash
cp .env.example .env
# Edit .env and add your GOOGLE_API_KEY
```

5. Run the planner:
```bash
# Run with default speed (no delay)
python main.py

# Run with 10-second delay between steps (recommended for learning)
python main.py --delay 10
```

## Project Structure 📁

```
react-agent-example/
├── main.py           # CLI entry point
├── agent.py          # Core ReAct implementation
├── tools.py          # Tool definitions
├── tool_executor.py  # Tool implementations
├── prompts.py        # System prompts
└── requirements.txt  # Dependencies
```

## How ReAct Works 🔧

1. **Agent receives a query**:
```
"Find a route from Boston to Miami"
```

2. **Agent thinks and chooses action**:
```json
{
    "thought": "I need to find available routes first",
    "action": {
        "name": "find_routes",
        "input": {
            "origin": "Boston, MA",
            "destination": "Miami, FL"
        }
    }
}
```

3. **Agent observes results and plans next step**:
```json
{
    "thought": "Now I should check conditions for route RT1234",
    "action": {
        "name": "check_conditions",
        "input": {
            "route_id": "RT1234"
        }
    }
}
```

4. **Agent makes final decision**:
```json
{
    "thought": "Based on conditions, RT1234 is optimal",
    "action": {
        "name": "dispatch_truck",
        "input": {
            "route_id": "RT1234"
        }
    }
}
```

## Example Interaction

This example shows how the agent processes a query through the ReAct framework:

```
==================== Iteration 1 ====================

🤔 Sending prompt to LLM:
------------------------------------------------------------
[System prompt with query and available tools]
------------------------------------------------------------

💭 Waiting for LLM response...

📝 LLM responded with:
------------------------------------------------------------
{
    "thought": "I need to find available routes first",
    "action": {
        "name": "find_routes",
        "input": {
            "origin": "Portland, OR",
            "destination": "Boston, MA"
        }
    }
}
------------------------------------------------------------

🔧 LLM requested tool execution:
------------------------------------------------------------
Tool: find_routes
Input parameters:
  - origin: Portland, OR
  - destination: Boston, MA
------------------------------------------------------------

⚙️ Executing tool...

📊 Tool execution results:
------------------------------------------------------------
{
    "routes": [
        {
            "id": "RT1498",
            "base_hours": 44,
            "via": "I-90"
        },
        {
            "id": "RT3021",
            "base_hours": 13,
            "via": "I-95"
        }
    ]
}
------------------------------------------------------------

==================== Iteration 2 ====================

[Process continues with checking conditions...]
```

### Understanding the Flow

1. **LLM Decision Making**:
   - The agent sends a prompt to the LLM (🤔)
   - The LLM thinks and decides what tool to use (📝)
   - The LLM provides structured instructions for tool execution

2. **Tool Execution**:
   - The agent receives LLM's instructions (🔧)
   - The agent executes the requested tool (⚙️)
   - The tool returns results (📊)
   - Results are fed back to the LLM for next decision

3. **Iteration Process**:
   - Each step is clearly logged with separators
   - You can see exactly what the LLM decided
   - You can see the exact tool inputs and outputs
   - The process repeats until a final answer is reached

The logging helps you understand:
- What the LLM is thinking
- Which tools it chooses and why
- What data is being passed to tools
- What results come back from tools
- How the LLM uses these results

## Extending the Framework

Add your own tools in 3 steps:

1. Define the tool interface in `tools.py`:
```python
NEW_TOOL = {
    "name": "my_tool_name",
    "description": "What the tool does",
    "parameters": {
        "param1": "Parameter description"
    }
}
```

2. Implement the logic in `tool_executor.py`:
```python
async def my_tool_name(self, params):
    # Your implementation here
    return {"result": "Tool output"}
```

3. The ReAct agent will automatically incorporate it into its reasoning!

## Understanding the Code

- `agent.py`: Core ReAct loop implementation
  - Think-Act-Observe cycle
  - Tool selection and execution
  - Response generation
  - Detailed logging of prompts and responses
  - Configurable execution delay

- `prompts.py`: System prompts that guide the agent
  - Task description
  - Response format
  - Decision-making guidance

- `tools.py`: Tool definitions
  - Interface specifications
  - Parameter schemas
  - Return type definitions

- `tool_executor.py`: Tool implementations
  - Business logic
  - Data processing
  - Result formatting

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.