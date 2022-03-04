# Check tuples with heterogeneous data types
temp_tuple = ("Srishti", "Jethy", 17, 4.2, "Kathmandu") # Possible to have heterogeneous data types in a tuple
print(f"Temp tuple: {temp_tuple}")

# Modify tuple
# temp_tuple[0] = "Sri" # This will not work
print(f"Temp tuple: {temp_tuple}")

new_tuple = ()
print(f"New tuple: {new_tuple}")


tuple_with_list = ("Srishti", "Jethy", 17, 4.2, "Kathmandu", [1, 2, 3])
print(f"Tuple with list: {tuple_with_list}")

tuple_with_list[5][0] = 4 # Immutable Tuple with Mutable List
print(f"Tuple with list: {tuple_with_list}")

# print all elements of tuples
for i in tuple_with_list:
    print(i)

# Join tuples with other types
tuple_with_list = tuple_with_list + (4, 5, 6)
print(f"Tuple with list: {tuple_with_list}")

# tuple_with_list = tuple_with_list + 6
print(f"Tuple with list: {tuple_with_list}")

tuple_with_list = tuple_with_list + (10,)
print(f"Tuple with list: {tuple_with_list}")

new_tuple = (1) + (2) # Only Consider as integers not tuple elements
print(f"New tuple: {new_tuple}")

new_tuple = (1,) + (2,) # Only Consider as tuple elements not integers
print(f"New tuple: {new_tuple}")

# Slicing
tuple_with_list = ("Srishti", "Jethy", 17, 4.2, "Kathmandu", [1, 2, 3])
first_3_element = tuple_with_list[:3]
print(f"First 3 element: {first_3_element}")

elements_from_last = tuple_with_list[-3:]
print(f"3 elements from last: {elements_from_last}")

#slicing with interval
print(f"Slicing with interval , Original tuple: {tuple_with_list}")
elements_from_2_to_4 = tuple_with_list[1:-1:2]
print(f"Elements from 2 to 4: {elements_from_2_to_4}")

#Reverse tuples
print(f"Reverse tuple: {tuple_with_list[::-1]}")

# Compare tuples
tuple1 = (11,2,3)
tuple2 = (6.0,1.2,2.1)

print(f"Compare tupl1 < tuple2: {tuple1 < tuple2}")

#max min value
print(f"Max value: {max(tuple1)}")
# print(f"Min value: {min(tuple_with_list)}") # Wont work 

# Unpoacking Tuple
def return_tuple(tuple_with_list):
    tuple_with_list = ("Srishti", "Jethy", 17, 4.2, "Kathmandu", [1, 2, 3])
    return tuple_with_list

new_value1,new_value2,new_value3,new_value4,new_value5,new_value6 = return_tuple(tuple_with_list)
print(f"New value1: {new_value1}")
print(f"New value2: {new_value2}")
print(f"New value3: {new_value3}")
print(f"New value4: {new_value4}")
print(f"New value5: {new_value5}")
print(f"New value6: {new_value6}")

# Indirect Tuple modification
tuple_with_list = ("Srishti", "Jethy", 17, 4.2, "Kathmandu", [1, 2, 3])
print(f"Tuple with list: {tuple_with_list}")

# Convert tuple to list
tuple_with_list = list(tuple_with_list)
print(f"Tuple with list: {tuple_with_list}")

#Modify element in the resulting list
tuple_with_list[0] = "Sri"
print(f"Tuple with list: {tuple_with_list}")

# Convert back to tuple
tuple_with_list = tuple(tuple_with_list)
print(f"Tuple with list: {tuple_with_list}")

