from abc import ABC, abstractmethod

# 1. Abstract base class
class SmartDevice(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def execute_command(self, command):
        pass

# 2. Concrete device classes overriding the abstract method
class SmartLight(SmartDevice):
    def execute_command(self, command):
        if command == "on":
            return f"{self.name} light is now ON."
        elif command == "off":
            return f"{self.name} light is now OFF."
        else:
            return f"{self.name} light: Unknown command."

class SmartThermostat(SmartDevice):
    def execute_command(self, command):
        try:
            temp = int(command)
            return f"{self.name} thermostat set to {temp}°C."
        except ValueError:
            return f"{self.name} thermostat: Invalid temperature."

class SmartSpeaker(SmartDevice):
    def execute_command(self, command):
        return f"{self.name} speaker is playing '{command}'."

# 3. Polymorphism in action
def command_center(devices, commands):
    for device, command in zip(devices, commands):
        print(device.execute_command(command))

# Example usage
light = SmartLight("Living Room")
thermostat = SmartThermostat("Bedroom")
speaker = SmartSpeaker("Kitchen")

devices = [light, thermostat, speaker]
commands = ["on", "22", "Jazz Music"]

command_center(devices, commands)
