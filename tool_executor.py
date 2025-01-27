"""
Tool implementations for the Logistics Route Planner.

This is a DEMO implementation that generates fake data!
In a real system, this would connect to real APIs and databases.
Instead, we generate random but realistic-looking data to show how it would work.

Each tool method follows this pattern:
1. Take input parameters
2. Generate realistic-looking fake data
3. Return a response that matches what a real API might return
"""

import random
from typing import Dict, Any
from datetime import datetime, timedelta

class ToolExecutor:
    """
    Executes our logistics tools with fake data generation.
    
    In a real system, this would:
    - Connect to real mapping services
    - Check real traffic APIs
    - Talk to a real fleet management system
    
    For this demo, we just generate realistic-looking fake data!
    """
    
    def __init__(self):
        """Set up our fake data generators with realistic options."""
        # Lists of highways to make routes look realistic
        self.major_highways = [
            "I-95",  # East Coast
            "I-75",  # Southeast
            "I-80",  # Northern cross-country
            "I-90",  # Northern cross-country
            "I-10",  # Southern cross-country
            "I-70"   # Midwest to West
        ]
        
        # Possible weather conditions for route checks
        self.weather_conditions = [
            "Clear skies",
            "Light rain", 
            "Heavy rain",
            "Snow flurries",
            "Heavy snow",
            "Fog",
            "High winds",
            "Severe thunderstorms"
        ]
        
        # Possible traffic events for route checks
        self.traffic_events = [
            "Construction",
            "Accident cleanup",
            "Heavy congestion",
            "Road work",
            "Lane closure",
            "Holiday traffic"
        ]
        
        # Data for generating fake truck assignments
        self.truck_prefixes = ["TRK", "VEH", "FRT"]  # Different types of trucks
        self.driver_first_names = ["John", "Sarah", "Mike", "Lisa", "David", "Emma"]
        self.driver_last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
    
    def _generate_route_id(self) -> str:
        """Create a random route ID like 'RT1234'."""
        return f"RT{random.randint(1000, 9999)}"
    
    def _generate_truck_id(self) -> str:
        """Create a random truck ID like 'TRK-123'."""
        prefix = random.choice(self.truck_prefixes)
        return f"{prefix}-{random.randint(100, 999)}"
    
    def _generate_driver(self) -> str:
        """Create a random driver name from our lists."""
        first = random.choice(self.driver_first_names)
        last = random.choice(self.driver_last_names)
        return f"{first} {last}"

    async def find_routes(self, params: Dict[str, Any]) -> Dict:
        """
        Find routes between two cities.
        
        In a real system, this would use a mapping API.
        For our demo, we generate 2-3 fake routes with:
        - Random but realistic-looking route IDs
        - Different estimated times
        - Major highways that would make sense
        """
        # Generate 2-3 different route options
        num_routes = random.randint(2, 3)
        routes = []
        
        for _ in range(num_routes):
            route_id = self._generate_route_id()
            base_hours = random.randint(8, 48)  # Between 8 and 48 hours
            # Pick 1-3 highways for the route
            via = random.sample(self.major_highways, k=random.randint(1, 3))
            
            routes.append({
                "route_id": route_id,
                "estimated_hours": base_hours,
                "via": " → ".join(via)  # Connect highways with arrows
            })
        
        return {
            "routes": routes,
            "origin": params["origin"],
            "destination": params["destination"]
        }

    async def check_conditions(self, params: Dict[str, Any]) -> Dict:
        """
        Check current conditions for a route.
        
        In a real system, this would check:
        - Real-time traffic APIs
        - Weather service APIs
        - Road work databases
        
        For our demo, we generate random but realistic delays and conditions.
        """
        # Generate plausible random delays
        traffic_delay = round(random.uniform(0, 4), 1)  # 0 to 4 hours
        weather_delay = round(random.uniform(0, 3), 1)  # 0 to 3 hours
        
        # Maybe add some conditions (not always)
        conditions = []
        if random.random() < 0.7:  # 70% chance of traffic event
            conditions.append(random.choice(self.traffic_events))
        if random.random() < 0.6:  # 60% chance of weather condition
            conditions.append(random.choice(self.weather_conditions))
        
        return {
            "route_id": params["route_id"],
            "traffic_delay_hours": traffic_delay,
            "weather_delay_hours": weather_delay,
            "conditions": " and ".join(conditions) if conditions else "No major conditions reported"
        }

    async def dispatch_truck(self, params: Dict[str, Any]) -> Dict:
        """
        Assign a truck and driver to a route.
        
        In a real system, this would:
        - Check available trucks
        - Check driver schedules
        - Make real assignments
        - Return real confirmation
        
        For our demo, we generate random but realistic-looking assignments.
        """
        # Create random but realistic-looking assignment
        truck_id = self._generate_truck_id()
        driver = self._generate_driver()
        
        # Set departure sometime in the next 6 hours
        departure_delta = timedelta(hours=random.uniform(0.5, 6))
        departure_time = (datetime.now() + departure_delta).strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "route_id": params["route_id"],
            "truck_id": truck_id,
            "driver": driver,
            "departure_time": departure_time,
            "status": "CONFIRMED"  # In real life, might be PENDING or FAILED
        } 