print('m' in 'animal')


text1 = "ladies"
text2 = "ladi"

print(len(text1))

if text1 == text2:
    print('Yes Maam, they are equal')
else:
    print('No Maam, they are not equal')

print(text1 == text2)

# print(chr(66))

# Slicing and dicing
name = "Sristhi Jethy"
print(name[0:3])

print(name[3:])

print(name[-1])

print(name[:-4])

# reverse the string
print(f"Reverse a string using name[::-1] = {name[::-1]}")
print(f"Reverse a string using name[::-2] = {name[::-2]}")

print(f"Print name with name[1:-1:2] = {name[1:-1:2]}")


# Split the string
name = "Sristhi Jethy"

full_name = name.split()
print(f"Result after split:{full_name}")

first_name = full_name[0] # First Item
last_name = full_name[1] # Second Item

print(f"First name: {first_name}")
print(f"Last name: {last_name}")

word = "Amazing"

print(word[-7:])

sentence = "I love India"

print(sentence.find('wove'))

print(sentence.find('love',1,len(sentence)))

sentence = "123IloveIndia"
print(sentence.isdigit())


string = "     I       love  India               "
print(string)
print(string.strip())
print("@".join(string.split()))

print(string.lstrip())
print(string.rstrip())

sentence = "The girl ladi is 15 years old ladi goes to school what a shame"
print(sentence.split('ladi')) # List, Mutable, Exclude the separator,Splits at all occurences

print(sentence.partition('ladi')) # Tuple , Immutable, includes the separator, Partitions only at the first occurence

ex_tuple = ('The girl ', 'ladi', ' is 15 years old ladi goes to school what a shame')
ex_list = ['The girl ', 'ladi', ' is 15 years old ladi goes to school what a shame']
print(ex_tuple[1])
# ex_tuple[1]= 'Sristhi'
# print(ex_tuple)

print(ex_list[1])
ex_list[1] = "Sristhi"
print(ex_list)