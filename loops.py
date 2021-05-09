"""
loops are used inaterate in sets, lists and disctionary
"""
# 1. For loop
# following is same method loop through in sets
names = ['Waleed', 'Ahmed', 'Annah', 'James']

for name in names:
    print(name)


# loops though destionary
person = {
    "name": "Waleed ur Rehman",
    "age": 19,
    "address": "PK"
}

for key, value in person.items():
    print(f"key:{key} value:{value}")

# for key in person:
#     print(f"key: {key}   value: {person[key]}")

# 2. while loop

number = 0

while number < 10:
    print(number)
    number +=1
else:
    print('else in while loop')

#Break and Continue

while number < 10:
    if number == 5:
        break
    number+=1
    print(number)
