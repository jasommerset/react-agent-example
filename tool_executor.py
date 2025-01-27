"""Tool implementations for the Logistics Route Planner."""

import random
from typing import Dict, Any
from datetime import datetime, timedelta

class ToolExecutor:
    """Executes tools and returns results."""
    
    def __init__(self):
        """Initialize the tool executor with route generation helpers."""
        # Route generation helpers
        self.major_highways = ["I-95", "I-75", "I-80", "I-90", "I-10", "I-70"]
        self.weather_conditions = [
            "Clear skies", "Light rain", "Heavy rain", "Snow flurries",
            "Heavy snow", "Fog", "High winds", "Severe thunderstorms"
        ]
        self.traffic_events = [
            "Construction", "Accident cleanup", "Heavy congestion",
            "Road work", "Lane closure", "Holiday traffic"
        ]
        
        # Truck and driver pool
        self.truck_prefixes = ["TRK", "VEH", "FRT"]
        self.driver_first_names = ["John", "Sarah", "Mike", "Lisa", "David", "Emma"]
        self.driver_last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia"]
    
    def _generate_route_id(self) -> str:
        """Generate a random route ID."""
        return f"RT{random.randint(1000, 9999)}"
    
    def _generate_truck_id(self) -> str:
        """Generate a random truck ID."""
        prefix = random.choice(self.truck_prefixes)
        return f"{prefix}-{random.randint(100, 999)}"
    
    def _generate_driver(self) -> str:
        """Generate a random driver name."""
        first = random.choice(self.driver_first_names)
        last = random.choice(self.driver_last_names)
        return f"{first} {last}"

    async def find_routes(self, params: Dict[str, Any]) -> Dict:
        """Find available routes between cities."""
        # Generate 2-3 fake routes with different times
        num_routes = random.randint(2, 3)
        routes = []
        
        for _ in range(num_routes):
            route_id = self._generate_route_id()
            base_hours = random.randint(8, 48)  # Random base time
            via = random.sample(self.major_highways, k=random.randint(1, 3))
            
            routes.append({
                "route_id": route_id,
                "estimated_hours": base_hours,
                "via": " → ".join(via)
            })
        
        return {
            "routes": routes,
            "origin": params["origin"],
            "destination": params["destination"]
        }

    async def check_conditions(self, params: Dict[str, Any]) -> Dict:
        """Check current conditions for a route."""
        # Generate random delays and conditions
        traffic_delay = round(random.uniform(0, 4), 1)
        weather_delay = round(random.uniform(0, 3), 1)
        
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
        """Dispatch a truck for a route."""
        # Generate random truck assignment
        truck_id = self._generate_truck_id()
        driver = self._generate_driver()
        
        # Random departure within next 6 hours
        departure_delta = timedelta(hours=random.uniform(0.5, 6))
        departure_time = (datetime.now() + departure_delta).strftime("%Y-%m-%d %H:%M:%S")
        
        return {
            "route_id": params["route_id"],
            "truck_id": truck_id,
            "driver": driver,
            "departure_time": departure_time,
            "status": "CONFIRMED"
        } 