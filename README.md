# ReAct Agent Example: The Fun Assistant 🎮

A simple example of building an AI agent using the ReAct (Reasoning and Acting) framework with Google's Gemini LLM. This example demonstrates how to create an agent that can:
1. Think about what to do
2. Choose and use tools
3. Provide fun responses!

## What is ReAct? 🤔

ReAct is a framework that helps AI agents:
- **Re**ason about what they should do
- Take **Act**ions using available tools
- Learn from the results

Think of it like playing a game:
1. Player sees the situation
2. Player thinks about what to do
3. Player uses an item or skill
4. Player sees what happened
5. Player decides what to do next

## Features 🌟

- Simple but complete ReAct implementation
- Two fun example tools:
  - `JokeFinder`: Discovers random jokes
  - `FortuneTeller`: Makes silly predictions
- Easy to extend with your own tools
- Built with Google's Gemini LLM
- Simple command-line interface

## Quick Start 🚀

1. Clone this repository:
```bash
git clone https://github.com/yourusername/react-agent-example.git
cd react-agent-example
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
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

5. Run the assistant:
```bash
python main.py
```

## Project Structure 📁

```
react-agent-example/
├── main.py           # CLI entry point
├── agent.py          # ReAct agent implementation
├── tools.py          # Tool definitions
├── tool_executor.py  # Tool implementations
├── prompts.py        # System prompts
└── requirements.txt  # Dependencies
```

## How It Works 🔧

1. **User types a query** like "Tell me a joke about programming"

2. **Agent thinks** about what to do:
```json
{
    "thought": "I should use the joke finder to get a programming joke",
    "action": {
        "name": "find_joke",
        "input": {
            "category": "programming"
        }
    }
}
```

3. **Agent uses tool** and gets result:
```json
{
    "joke": "Why do programmers prefer dark mode? Because light attracts bugs!"
}
```

4. **Agent provides answer**:
```json
{
    "thought": "That's a good programming joke!",
    "answer": "Here's a funny programming joke: Why do programmers prefer dark mode? Because light attracts bugs! 😄"
}
```

## Available Tools 🛠️

### 1. JokeFinder
```python
{
    "name": "find_joke",
    "description": "Find a random joke, optionally by category",
    "parameters": {
        "category": "Type of joke (optional): programming, general, dad_joke"
    }
}
```

### 2. FortuneTeller
```python
{
    "name": "tell_fortune",
    "description": "Get a silly prediction about your future",
    "parameters": {
        "topic": "What to predict: career, love, general"
    }
}
```

## Example Interactions 💬

```
Your query: Tell me a programming joke
🤔 Thinking...
💭 I should use the joke finder to get a programming joke
🔧 Using tool: find_joke
😄 Here's a funny programming joke: Why do programmers prefer dark mode? Because light attracts bugs!

Your query: What's in my future?
🤔 Thinking...
💭 I'll consult the fortune teller for a general prediction
🔧 Using tool: tell_fortune
🔮 According to my crystal ball, you will soon debug the most mysterious code bug of your life... 
   it turns out it was just a missing semicolon all along!

Your query: exit
👋 Goodbye! Have a great day!
```

## Extending the Agent 🔌

Add your own tools in 3 easy steps:

1. Define tool in `tools.py`:
```python
MY_TOOL = {
    "name": "my_tool",
    "description": "What my tool does",
    "parameters": {
        "param1": "Description of param1"
    }
}
```

2. Implement in `tool_executor.py`:
```python
async def my_tool(self, params):
    # Your implementation here
    return {"result": "Something fun!"}
```

3. The agent will automatically be able to use it!

## License 📄

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments 🙏

- Inspired by the ReAct paper: [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
- Built with Google's Gemini LLM
- Made with ❤️ for learning and fun! 