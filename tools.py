"""Tool definitions for the Fun Assistant."""

# List of available tools
TOOLS = [
    {
        "name": "find_joke",
        "description": """
Find a random joke to make someone laugh! You can specify a category for a more specific type of joke.

Example categories:
- programming: Jokes about coding and software
- general: Any kind of joke
- dad_joke: Classic dad jokes

The tool will return a joke as a string.
        """.strip(),
        "parameters": {
            "type": "object",
            "properties": {
                "category": {
                    "type": "string",
                    "description": "Type of joke to find",
                    "enum": ["programming", "general", "dad_joke"]
                }
            }
        }
    },
    {
        "name": "tell_fortune",
        "description": """
Get a silly prediction about the future! Specify a topic to get a more focused fortune.

Example topics:
- career: Job and professional life
- love: Relationships and romance
- general: Any kind of prediction

The tool will return a fortune as a string.
        """.strip(),
        "parameters": {
            "type": "object",
            "properties": {
                "topic": {
                    "type": "string",
                    "description": "What to make a prediction about",
                    "enum": ["career", "love", "general"]
                }
            }
        }
    }
] 