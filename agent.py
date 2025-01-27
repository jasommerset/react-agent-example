"""ReAct Agent implementation using Google's Gemini."""

import json
import os
from typing import Dict, List, Any
import logging
import re

import google.generativeai as genai
from dotenv import load_dotenv

from tools import TOOLS
from tool_executor import ToolExecutor
from prompts import SYSTEM_PROMPT

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class Agent:
    """ReAct agent that processes queries using think-act-observe cycle."""
    
    def __init__(self):
        """Initialize the agent with tools and LLM."""
        # Load environment variables
        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")
        if not api_key:
            raise ValueError("GOOGLE_API_KEY environment variable is not set")
            
        # Configure Gemini
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.7,
                "top_p": 0.8,
                "top_k": 40,
            }
        )
        
        # Initialize tools and history
        self.tool_executor = ToolExecutor()
        self.history: List[str] = []
        self.max_iterations = 5
        
    async def process_query(self, query: str) -> Dict[str, Any]:
        """Process a query using the ReAct loop."""
        self.history = []  # Reset history for new query
        iteration = 0
        
        while iteration < self.max_iterations:
            iteration += 1
            logger.info(f"Iteration {iteration}")
            
            try:
                # Prepare prompt
                prompt = SYSTEM_PROMPT.format(
                    query=query,
                    history=self._format_history(),
                    tools=json.dumps(TOOLS, indent=2)
                )
                
                # Get LLM response
                logger.info("Getting LLM response...")
                response = await self.model.generate_content_async(prompt)
                
                # Parse response
                thought = response.text.strip()
                logger.info(f"Raw response:\n{thought}")
                
                # Extract JSON from code blocks if present
                if "```" in thought:
                    blocks = thought.split("```")
                    # Take the content of the first code block
                    thought = blocks[1] if len(blocks) > 1 else blocks[0]
                    thought = thought.replace('json', '').strip()
                
                logger.info(f"Extracted content:\n{thought}")
                
                try:
                    parsed = json.loads(thought)
                except json.JSONDecodeError as je:
                    logger.error(f"JSON parse error: {je}")
                    raise
                
                # If we have a final answer, return it
                if "answer" in parsed:
                    self.history.append(f"Assistant: {parsed['answer']}")
                    return parsed
                
                # Otherwise, execute the tool
                if "action" in parsed:
                    tool_name = parsed["action"]["name"]
                    tool_input = parsed["action"]["input"]
                    
                    # Execute tool
                    logger.info(f"Executing tool: {tool_name}")
                    result = await getattr(self.tool_executor, tool_name)(tool_input)
                    
                    # Add result to history
                    observation = f"Tool '{tool_name}' returned: {json.dumps(result)}"
                    self.history.append(observation)
                    continue
                
                raise ValueError("Response missing both 'answer' and 'action'")
                
            except Exception as e:
                logger.error(f"Error in iteration {iteration}: {e}")
                return {
                    "thought": "Error occurred",
                    "answer": f"I encountered an error: {str(e)}"
                }
        
        return {
            "thought": "Maximum iterations reached",
            "answer": "I apologize, but I couldn't find a satisfactory answer within the allowed iterations."
        }
    
    def _format_history(self) -> str:
        """Format conversation history for the prompt."""
        return "\n".join(self.history) if self.history else "No previous observations." 