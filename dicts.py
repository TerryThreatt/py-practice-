
# data structure - similar to javascript objects - key/value pairs

user_info = {"city": "Paris", "temperature": 59.0, "is_raining": True}


print(user_info["city"])

user_info.values()


for v in user_info.values():
    print(v)

for k,v in user_info.items():
    print(f"key: {k}, value: {v}" )


print("city" in user_info.keys())

# methods

# Clear - clears all keys/values
user_info.clear()

# Copy - copies all keys/values
u = user_info.copy()
u #=> user_info = {"city": "Paris", "temperature": 59.0, "is_raining": True}

# Fromkeys -  grabs key and sets value
user_info.fromkeys(["city"], 'Idabel')

# Get - get key in object
user_info.get("city") #=> 'Idabel'

# Pop - removes key off dictionary
user_info.pop()

# PopItem - removes multiple key off dictionary
user_info.popitem("")

# Update - update key off dictionary
user_info.update("")
