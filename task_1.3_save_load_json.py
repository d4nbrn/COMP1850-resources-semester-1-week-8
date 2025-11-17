import json

# Data to save
data = {
    "userId": 102,
    "name": "Bob Brown",
    "email": "bob.brown@example.co.uk",
    "isActive": True
}

# Save the data to a file named "user.json"
with open("user.json", "w") as f:
    json.dump(data, f)

# Load the data back from "user.json"
with open("user.json", "r") as f:
    loaded_data = json.load(f)

print(f"Here is the json file: {loaded_data}")
