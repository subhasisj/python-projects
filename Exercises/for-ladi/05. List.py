sample_list = []  # Create a list
another_list = list()  # Create a list

sample_list.append(1)
sample_list.append(2)  # appending a single element

sample_list.extend([4, 5])  # Append the list with an iterable (a new sequence)

natural_number_upto_10 = [i for i in range(10)]  # List Comprehension

print(natural_number_upto_10)

# Nested list
nested_list = [1, 2, 3, [4, 5, 6], [7, 8, 9]]
print(nested_list[4][1])  # access nested list
print(nested_list[-1][-1])  # Last element of last element

sample_command = "sample_list.append('100000')"

eval(sample_command)  # Evaluate the string as a Python expression
print(sample_list)

# membership

print("ladi" in sample_list)
print("100000" in sample_list)
print(100000 in sample_list)
name = "Srishti Jethy"

first_name, last_name = name.split()
print(first_name)
print(last_name)

print(f"First Name: {first_name}")
print("First name:" + first_name, "\t" + "Last Name: " + last_name)

first = ["a", "b", "c"]
another = [4, 1, 6]
last = [1, 2, 3]

print(nested_list > last)

# Using slices for list modification
print(f"Natural number upto 10: {natural_number_upto_10}")

natural_number_upto_10[0] = 100
natural_number_upto_10[1:3] = [200, 300]
natural_number_upto_10[4:8] = "Ladi"
print(f"Natural number upto 10: {natural_number_upto_10}")
natural_number_upto_10[2:] = "Monty"
print(f"Natural number upto 10: {natural_number_upto_10}")
# Pointers
temp_list = natural_number_upto_10  # Shallow copy
temp_list[0] = "500"
print(f"Temp list: {temp_list}")
print(f"Natural number upto 10: {natural_number_upto_10}")

temp_list = natural_number_upto_10.copy()  # Deep copy
temp_list[0] = "3000"
print(f"Temp list: {temp_list}")
print(f"Natural number upto 10: {natural_number_upto_10}")

# using [:] for copying
temp_list = natural_number_upto_10[:]
temp_list[0] = "101"
print(f"Temp list: {temp_list}")
print(f"Natural number upto 10: {natural_number_upto_10}")

# using list() to copy
print(f"Natural number upto 10 (Before): {natural_number_upto_10}")
temp_list = list(natural_number_upto_10)
temp_list[0] = "201"
print(f"Temp list: {temp_list}")
print(f"Natural number upto 10: {natural_number_upto_10}")

temp_list = list(
    "ladi"
)  # list() can take a string as well and will automatically convert it to a list
print(f"Temp list: {temp_list}")
temp_list = list("467")
print(f"Temp list: {temp_list}")

#Keep a dictionary in a list
temp_list = [
    {
        "name": "Srishti Jethy",
        "age": 17,
        "address": "Kathmandu",
    }
]

print(f"Temp list: {temp_list}")
# print only age information
print(f"Temp list: {temp_list[0]['age']}") # Dictionary["key"]

# index function
print(f"Natural number upto 10: {natural_number_upto_10}")
index_of_variable = natural_number_upto_10.index("M")
print(f"Index of M: {index_of_variable}")
index_of_variable = natural_number_upto_10.index(100)
print(f"Index of 100: {index_of_variable}")