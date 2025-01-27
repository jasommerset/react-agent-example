"""Command line interface for the ReAct agent."""

import asyncio
import argparse
import logging
from typing import Optional

from agent import Agent

# Set up clean logging - just show the message without prefixes
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',  # Only show the message part
    force=True  # Override any existing configuration
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
    """Print welcome message."""
    print("\n" + "=" * 40)
    print("LOGISTICS ROUTE PLANNER")
    print("=" * 40)
    print("\nThis tool helps you plan and dispatch truck routes.")
    print("\nYou can:")
    print("- Find routes between cities")
    print("- Check traffic and weather conditions")
    print("- Dispatch trucks and drivers")
    print("\nExample queries:")
    print('- "Find a route from Seattle to Chicago"')
    print('- "What\'s the fastest way to ship from Miami to Boston?"')
    print('- "I need to transport goods from LA to NYC"')
    print("\nType 'exit' to quit")
    print("=" * 40 + "\n")

async def main():
    # Set up command line arguments
    parser = argparse.ArgumentParser(description='Run the logistics route planner')
    parser.add_argument('--delay', type=float, default=0,
                      help='Delay in seconds between steps (default: 0)')
    args = parser.parse_args()
    
    # Initialize agent with configured delay
    agent = Agent(delay_seconds=args.delay)
    
    print_welcome()
    
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