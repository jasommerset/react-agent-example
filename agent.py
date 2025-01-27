"""
A simple demonstration of a ReAct (Reasoning + Acting) agent using Google's Gemini LLM.

This is a tutorial implementation meant for learning purposes only.
It shows how an AI can:
1. Think about what to do (Reasoning)
2. Use tools to do it (Acting)
3. Learn from the results (Observing)

Not meant for production use - just a learning tool!
"""

import json
import os
import asyncio
from typing import Dict, List, Any
import logging

# Google's Gemini AI library
import google.generativeai as genai
from dotenv import load_dotenv

# Our tool definitions and implementations
from tools import TOOLS
from tool_executor import ToolExecutor
from prompts import SYSTEM_PROMPT

# Set up clean logging - just show the message without prefixes
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',  # Only show the message part
    force=True  # Override any existing configuration
)
logger = logging.getLogger(__name__)

class Agent:
    """
    A simple ReAct agent that can:
    1. Understand user queries
    2. Think about what tools to use
    3. Use those tools
    4. Learn from the results
    
    This is a learning example only - not meant for production use!
    """
    
    def __init__(self, delay_seconds: float = 0):
        """
        Set up our agent with:
        - Google's Gemini AI
        - Our available tools
        - Optional delay to make it easier to follow what's happening
        
        Args:
            delay_seconds: How long to pause between steps (helps you read the output)
        """
        # Load our API key from the .env file
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("Please add your GOOGLE_API_KEY to the .env file!")
            
        # Set up Gemini AI with some basic settings
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.7,  # How creative should the AI be (0.0-1.0)
                "top_p": 0.8,        # How focused should responses be (0.0-1.0)
                "top_k": 40,         # How many options to consider
            }
        )
        
        # Initialize our tools and conversation history
        self.tool_executor = ToolExecutor()
        self.history: List[str] = []        # Keep track of what's happened
        self.max_iterations = 10            # Don't let it loop forever
        self.delay_seconds = delay_seconds  # Optional delay between steps
        
    async def process_query(self, query: str) -> Dict[str, Any]:
        """
        Process a user's question using the ReAct loop:
        1. Think about what to do
        2. Use a tool or give an answer
        3. Learn from the result
        4. Repeat until we have a final answer
        
        Args:
            query: The user's question
            
        Returns:
            A dictionary with the final answer or error message
        """
        self.history = []  # Start fresh for each new query
        iteration = 0      # Keep track of how many steps we've taken
        
        # Keep going until we have an answer or hit our limit
        while iteration < self.max_iterations:
            iteration += 1
            logger.info(f"\n{'='*20} Iteration {iteration} {'='*20}")
            
            try:
                # 1. Create the prompt for the AI
                # This includes:
                # - The user's question
                # - What's happened so far
                # - What tools are available
                prompt = SYSTEM_PROMPT.format(
                    query=query,
                    history=self._format_history(),
                    tools=json.dumps(TOOLS, indent=2)
                )
                
                # Optional delay to help you read what's happening
                if self.delay_seconds > 0:
                    await asyncio.sleep(self.delay_seconds)
                
                # 2. Send the prompt to the AI
                logger.info("\n🤔 Sending prompt to LLM:")
                logger.info("-" * 60)
                logger.info(prompt)
                logger.info("-" * 60)
                
                # 3. Get the AI's response
                response = await self.model.generate_content_async(prompt)
                
                # 4. Clean up and log the response
                thought = response.text.strip()
                logger.info("\n📝 LLM responded with:")
                logger.info("-" * 60)
                logger.info(thought)
                logger.info("-" * 60)
                
                # 5. Extract the JSON from code blocks if present
                if "```" in thought:
                    blocks = thought.split("```")
                    thought = blocks[1] if len(blocks) > 1 else blocks[0]
                    thought = thought.replace('json', '').strip()
                
                # 6. Parse the response as JSON
                try:
                    parsed = json.loads(thought)
                except json.JSONDecodeError as je:
                    error_msg = f"Error parsing JSON response: {je}"
                    logger.error(error_msg)
                    self.history.append(f"Error: {error_msg}")
                    continue
                
                # 7. If we have a final answer, we're done!
                if "answer" in parsed:
                    logger.info("\n✨ LLM provided final answer:")
                    logger.info("-" * 60)
                    logger.info(parsed["answer"])
                    logger.info("-" * 60)
                    self.history.append(f"Assistant: {parsed['answer']}")
                    return parsed
                
                # 8. Otherwise, we need to use a tool
                if "action" in parsed:
                    tool_name = parsed["action"]["name"]
                    tool_input = parsed["action"]["input"]
                    
                    # Log what tool the AI wants to use
                    logger.info("\n🔧 LLM requested tool execution:")
                    logger.info("-" * 60)
                    logger.info(f"Tool: {tool_name}")
                    logger.info(f"Input parameters:")
                    for key, value in tool_input.items():
                        logger.info(f"  - {key}: {value}")
                    logger.info("-" * 60)
                    
                    # Optional delay before running the tool
                    if self.delay_seconds > 0:
                        await asyncio.sleep(self.delay_seconds)
                    
                    try:
                        # 9. Run the tool
                        logger.info("\n⚙️ Executing tool...")
                        result = await getattr(self.tool_executor, tool_name)(tool_input)
                        
                        # 10. Log the results
                        logger.info("\n📊 Tool execution results:")
                        logger.info("-" * 60)
                        logger.info(json.dumps(result, indent=2))
                        logger.info("-" * 60)
                        
                        # 11. Add the result to our history
                        observation = f"Tool '{tool_name}' returned: {json.dumps(result)}"
                        self.history.append(observation)
                    except AttributeError as e:
                        # Handle case where the AI tries to use a tool that doesn't exist
                        error_msg = f"Tool '{tool_name}' is not available. Please use only: {', '.join(tool for tool in dir(self.tool_executor) if not tool.startswith('_'))}"
                        logger.error(error_msg)
                        self.history.append(f"Error: {error_msg}")
                    except Exception as e:
                        # Handle any other tool errors
                        error_msg = f"Error executing tool '{tool_name}': {str(e)}"
                        logger.error(error_msg)
                        self.history.append(f"Error: {error_msg}")
                    continue
                
                # If we get here, the AI's response wasn't valid
                error_msg = "Response missing both 'answer' and 'action'"
                logger.error(error_msg)
                self.history.append(f"Error: {error_msg}")
                continue
                
            except Exception as e:
                # Handle any other unexpected errors
                error_msg = f"Unexpected error: {str(e)}"
                logger.error(error_msg)
                self.history.append(f"Error: {error_msg}")
                continue
        
        # If we get here, we tried too many times without getting an answer
        logger.warning("Maximum iterations reached without resolution")
        return {
            "thought": "Maximum iterations reached",
            "answer": "I apologize, but I couldn't find a satisfactory answer within the allowed iterations."
        }
    
    def _format_history(self) -> str:
        """
        Format the conversation history into a string.
        This helps the AI remember what has happened so far.
        """
        return "\n".join(self.history) if self.history else "No previous observations." 