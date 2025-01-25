"""CLI interface for the ReAct Agent."""

import asyncio
import logging
from typing import Optional

from agent import Agent

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s'  # Simple format for CLI
)
logger = logging.getLogger(__name__)

def print_separator(title: str = "", char: str = "-", width: int = 80):
    """Print a separator line with optional title."""
    if title:
        print(f"\n{char * width}")
        print(f"{title.center(width)}")
        print(f"{char * width}\n")
    else:
        print(f"\n{char * width}\n")

def print_welcome():
    """Print a welcome message."""
    print_separator("WELCOME TO REACT AGENT EXAMPLE", "=")
    print("This is a demonstration of the ReAct framework using Google's Gemini.")
    print("\nAvailable tools:")
    print("1. Tell jokes (programming, general, or dad jokes)")
    print("2. Predict your future (career, love, or general)")
    print("\nType 'exit' to quit.")
    print_separator()

async def main():
    """Run the ReAct Agent CLI."""
    print_welcome()
    
    # Initialize agent
    agent = Agent()
    
    while True:
        try:
            # Get user input
            query = input("\nYour query: ").strip()
            if not query:
                print("Please type something!")
                continue
                
            if query.lower() == "exit":
                print_separator("GOODBYE!", "=")
                print("Thanks for trying the ReAct Agent!")
                break
                
            # Process query
            print_separator("NEW QUERY", "-")
            response = await agent.process_query(query)
            
            # Show final response
            print_separator("RESPONSE", "-")
            if "answer" in response:
                print(response["answer"])
                
        except Exception as e:
            logger.error(f"Error: {str(e)}")
            print("\nTip: If this is an API error, check your GOOGLE_API_KEY in .env")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("\nInterrupted by user. Goodbye!") 