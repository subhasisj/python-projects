sample_list = []
another_list = list()

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
 
eval(sample_command) # Evaluate the string as a Python expression
print(sample_list)

# membership

print('ladi' in sample_list)
print('100000' in sample_list)
print(100000 in sample_list)
name = "Srishti Jethy"

first_name, last_name = name.split() 
print(first_name)
print(last_name)

print(f"First Name: {first_name}")
print("First name:"+ first_name , "\t" + "Last Name: " + last_name)

first = ["a","b","c"]
another = [4,1,6]
last = [1,2,3]

print(nested_list > last)         
