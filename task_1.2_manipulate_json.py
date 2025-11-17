import json

# Original JSON data (fixed boolean)
data = """{
    "userId": 101,
    "name": "Alice Smith",
    "roles": ["admin", "editor"],
    "isActive": true
}"""

# Modify the "isActive" field and add "viewer" to roles
data_ = json.loads(data)
data_["isActive"] = False
data_["roles"].append("viewer")

# Convert back to JSON string and print
print(json.dumps(data_, indent=4))
