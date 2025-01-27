"""Tool definitions for the Logistics Route Planner."""

# List of available tools
TOOLS = [
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
                "origin": {
                    "type": "string",
                    "description": "Starting city"
                },
                "destination": {
                    "type": "string",
                    "description": "Destination city"
                }
            },
            "required": ["origin", "destination"]
        }
    },
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
                "route_id": {
                    "type": "string",
                    "description": "Route identifier"
                }
            },
            "required": ["route_id"]
        }
    },
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
                "route_id": {
                    "type": "string",
                    "description": "Route identifier"
                }
            },
            "required": ["route_id"]
        }
    }
] 