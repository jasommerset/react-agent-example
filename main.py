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
    print_separator("LOGISTICS ROUTE PLANNER", "=")
    print("This tool helps plan and dispatch truck routes using the ReAct framework.")
    print("\nCapabilities:")
    print("1. Find available routes between cities")
    print("2. Check current traffic and weather conditions")
    print("3. Dispatch trucks and confirm assignments")
    print("\nExample queries:")
    print('- "Find a route from Boston to Miami"')
    print('- "What\'s the best route from NYC to LA with current conditions?"')
    print('- "Dispatch a truck from Chicago to Houston"')
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