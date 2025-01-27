"""
Tool definitions for the Logistics Route Planner.

This file defines what tools are available to the AI. Each tool has:
1. A name - what to call it
2. A description - what it does and what information it needs
3. Parameters - what information it needs and in what format

This is just the definition of the tools - the actual code that runs them
is in tool_executor.py
"""

# List of all available tools the AI can use
TOOLS = [
    # Tool 1: Find available shipping routes
    {
        "name": "find_routes",
        "description": """
Find available shipping routes between two cities. Returns multiple route options with estimated base times.

Parameters:
- origin: Starting city (e.g. "Boston, MA")
- destination: End city (e.g. "Miami, FL")

Returns a list of route objects with:
- route_id: Unique identifier
- estimated_hours: Base travel time without delays
- via: Major cities or highways on route
        """.strip(),
        "parameters": {
            "type": "object",
            "properties": {
                # The city we're starting from
                "origin": {
                    "type": "string",
                    "description": "Starting city"
                },
                # The city we're going to
                "destination": {
                    "type": "string",
                    "description": "Destination city"
                }
            },
            "required": ["origin", "destination"]  # Both cities are required
        }
    },
    
    # Tool 2: Check current road conditions
    {
        "name": "check_conditions",
        "description": """
Check current traffic and weather conditions for a specific route.

Parameters:
- route_id: Route identifier from find_routes

Returns conditions object with:
- traffic_delay_hours: Current traffic delays
- weather_delay_hours: Expected weather-related delays
- conditions: Description of major conditions affecting route
        """.strip(),
        "parameters": {
            "type": "object",
            "properties": {
                # Which route to check (must be from find_routes first)
                "route_id": {
                    "type": "string",
                    "description": "Route identifier"
                }
            },
            "required": ["route_id"]  # Route ID is required
        }
    },
    
    # Tool 3: Assign and dispatch a truck
    {
        "name": "dispatch_truck",
        "description": """
Assign a truck to a specific route and confirm the dispatch.

Parameters:
- route_id: Route identifier from find_routes

Returns dispatch object with:
- truck_id: Assigned truck identifier
- driver: Driver information
- departure_time: Scheduled departure
- status: Dispatch confirmation status
        """.strip(),
        "parameters": {
            "type": "object",
            "properties": {
                # Which route to dispatch a truck for
                "route_id": {
                    "type": "string",
                    "description": "Route identifier"
                }
            },
            "required": ["route_id"]  # Route ID is required
        }
    }
] 