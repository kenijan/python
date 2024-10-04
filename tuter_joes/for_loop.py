
# for_loop

'''

Syntax: for variable in sequence:
             # Code block to be executed

       variable: The loop variable that takes the value of each item in the sequence.
       sequence: A collection (such as a list, tuple, string, or range,etc) to iterate over.

'''
#list

fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)

# range

for i in range(3):
    print(i)
# string

for char in "hello":
    print(char)

# Looping through a dictionary:

person = {"name": "Kenijan", "age": 18, "city": "Colombo"}
for key, value in person.items():
    print(f"{key}: {value}")