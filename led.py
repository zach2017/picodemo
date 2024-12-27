from machine import Pin
import rp2
import json
print("here")
# Ensure Pin 25 Low...
thePin=Pin("LED", Pin.OUT)


# Method 1: Using regular files
def save_to_file():
    # Open file in write mode - creates file if it doesn't exist
    # with open("data.txt", "w") as file:
    #     file.write("Hello from Pico!")
    
    # Reading the data back
    with open("data.txt", "r") as file:
        data = file.read()
        print("Read from file:", data)

# Method 2: Using JSON for structured data


def save_structured_data():
    # Example data structure

    data = {

        "sensor_readings": [20.5, 21.0, 21.5],
        "device_name": "zaapico2",
        "is_active": True
    }
    
    # Save to JSON file
    #with open("config.json", "w") as file:
    #
    #     json.dump(data, file)
    
    # Read JSON data back
    with open("config.json", "r") as file:
        loaded_data = json.load(file)
        print("Loaded config:", loaded_data)
        thePin.value(loaded_data)

# Example usage
if __name__ == "__main__":
    # Example 1: Simple file storage
    save_to_file()
    
    # Example 2: JSON storage
    save_structured_data()
    
    # Example 3: Flash memory
    # Be careful with flash memory - it has limited write cycles
    print("foo")

    # Note: For production use, consider wear leveling and error checking