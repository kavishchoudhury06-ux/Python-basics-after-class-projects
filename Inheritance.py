class Vehicle:
    def __init__(self, name, max_speed, mileage, capacity):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
        self.capacity = capacity

    def calculate_fare(self):
        return 50 * self.capacity

class Bus(Vehicle):
    def calculate_fare(self):
        base_fare = super().calculate_fare()
        total_fare = base_fare * 1.1  
        return total_fare

# Create an instance of Bus
school_bus = Bus("School Volvo", 120, 18, 50)

# Print details
print(f"Vehicle Name: {school_bus.name}")
print(f"Capacity: {school_bus.capacity}")
print(f"Total Fare: ${school_bus.calculate_fare():.2f}")
