"""Tool implementations for the Fun Assistant."""

import random
from typing import Dict, Any

class ToolExecutor:
    """Executes tools and returns results."""
    
    def __init__(self):
        """Initialize the tool executor with some fun canned responses."""
        self.programming_jokes = [
            "Why do programmers prefer dark mode? Because light attracts bugs!",
            "Why did the programmer quit his job? Because he didn't get arrays!",
            "What's a programmer's favorite hangout spot? The Foo Bar!",
            "Why do programmers always mix up Halloween and Christmas? Because Oct 31 == Dec 25!",
            "Why was the JavaScript developer sad? Because he didn't Node how to Express himself!"
        ]
        
        self.general_jokes = [
            "What do you call a bear with no teeth? A gummy bear!",
            "Why don't eggs tell jokes? They'd crack up!",
            "What do you call a fake noodle? An impasta!",
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "What do you call a can opener that doesn't work? A can't opener!"
        ]
        
        self.dad_jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fish wearing a bowtie? So-fish-ticated!",
            "How do you organize a space party? You planet!",
            "What do you call a bear with no ears? B!",
            "Why did the cookie go to the doctor? Because it was feeling crumbly!"
        ]
        
        self.career_fortunes = [
            "You will debug the most mysterious code bug of your life... it was just a missing semicolon!",
            "Your next pull request will be approved without any comments... in your dreams!",
            "You will become the official Stack Overflow answerer for your team!",
            "Your code will run perfectly on the first try... just kidding!",
            "You will invent a new programming language that only uses emojis!"
        ]
        
        self.love_fortunes = [
            "You will find true love at a Python meetup!",
            "Your soulmate will debug your code without asking a single question!",
            "You will meet someone who loves semicolons as much as you do!",
            "Your next date will be with someone who actually understands regex!",
            "You will find someone who appreciates your variable naming conventions!"
        ]
        
        self.general_fortunes = [
            "You will finally understand why it's called JavaScript!",
            "Your rubber duck will become sentient and start giving coding advice!",
            "You will discover a new coffee brewing algorithm that maximizes coding efficiency!",
            "Your computer will start understanding your thoughts... and judge your code silently!",
            "You will become fluent in binary... in your sleep!"
        ]

    async def find_joke(self, params: Dict[str, Any]) -> Dict[str, str]:
        """Return a random joke from the specified category."""
        category = params.get("category", "general")
        
        if category == "programming":
            joke = random.choice(self.programming_jokes)
        elif category == "dad_joke":
            joke = random.choice(self.dad_jokes)
        else:
            joke = random.choice(self.general_jokes)
            
        return {"joke": joke}

    async def tell_fortune(self, params: Dict[str, Any]) -> Dict[str, str]:
        """Return a silly prediction about the future."""
        topic = params.get("topic", "general")
        
        if topic == "career":
            fortune = random.choice(self.career_fortunes)
        elif topic == "love":
            fortune = random.choice(self.love_fortunes)
        else:
            fortune = random.choice(self.general_fortunes)
            
        return {"fortune": fortune} 