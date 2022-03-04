# Dictionary Creation
dictionary = {
    "name": "Srishti Jethy",  # "Key" : "Value"
    "age": 17,
    "address": "Kathmandu",
}

print(f"Dictionary: {dictionary}")

# unpack elements of Dictionary


def dummy_function(name, age, address):
    print(f"Name: {name}")
    print(f"Age: {age}")
    print(f"Address: {address}")


dummy_function("srishti", 17, "kathmandu")

dummy_function(**dictionary)  # Unpacking keyword arguments

# modify elements
dictionary["age"] = 18
print(f"Dictionary: {dictionary}")

dictionary["address1"] = "OdishA"
print(f"Dictionary: {dictionary}")

# nested Dictionary
dictionary = {
    "name": "Srishti Jethy",  # "Key" : "Value"
    "age": 17,
    "address": "Kathmandu",
    "address1": {
        "city": "Odisha",
        "state": "Odisha",
        "country": "India",
    },
}

multi_dictionary = [
    {"name": "Srishti Jethy", "age": 17, "address": "Kathmandu"},
    {"name": "Subhasis Jethy", "age": 33, "address": "Odisha"}
]
print(f"Dictionary: {multi_dictionary}")

# Sort multi_dictionary by Age
multi_dictionary.sort(key=lambda x: x["age"],reverse=True) # Sort by the age key
print(f"Dictionary: {multi_dictionary}")

employee = {
    "name": "Srishti Jethy",
    "age": 17,
    "address": "Kathmandu",
        "city": "    "address1": {
Odisha",
        "state": "Odisha",
        "country": "India",
    },
}

#print using loop
for key, value in employee.items():
    print(f"Key: {key}")
    print(f"Value: {value}")

