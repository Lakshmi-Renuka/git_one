
for x in range(4):
    for y in range(3):
        print(f"({x},{y})")

n = [5,2,5,2,2]
for i in n:
    print('x' * i)

n = [3,6,2,8,4,10] 
max = n[0]
for i in n:
    if i > max:
        max = i 
print(max)

customers = [
    {"name": "John", "age": 25, "is verified": True},
    {"name": "Jane", "age": 30, "is verified": False},
    {"name": "Bob", "age": 35, "is verified": True}
]   
print(customers[0]["name"])

phone_number = input("Enter your phone number: ")
mapping = { "1": "One", "2": "Two", "3": "Three", "4": "Four","5": "Five","6": "Six", "7": "Seven", "8": "Eight", "9": "Nine",  "0": "Zero"}
for digit in phone_number:
    print(mapping.get(digit, digit), end=" ")