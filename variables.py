# ----------The Basics----------

# 1. Variables
# NAME, AGE = 'WALEED', 20
name = 'waleed'
age = 19
pi = 3.14
number = [1, 2, 3, 4]


print(name)
print(age)
print(pi)
print(number)


# 2. Naming Variables

name = 'waleed'
fullName = 'Waleed ur Rehman'  # camalCase
full_name = 'Waleed ur Rehman'
AGE = 25
PI = 3.14

# 3. Data Types

brand = 'clever tech'  # str = string
age = 4  # int = integer
pi = 3.14  # float  = decimal number
numbers = []  # [] = list
isAdult = True  # True, False = Boolean


print(type(brand))  # type() function show the data type of variables
print(type(age))
print(type(pi))
print(type(numbers))
print(type(isAdult))


# 3. Dynamically Typed

brand: str = 'Clever Tech'
isAdult: bool = True


def hello() -> str:  # This method return string
    return 'helo'


def number() -> int:  # This method return integer
    return 1

# 4. Strings


brand = 'Clever Tech'

print(brand.upper())  # All letters in upper case
print(brand.lower())  # All letters in lower case
print(brand.replace('C', 'A'))  # Replace the letter you want
print(len(brand))  # Find the length of caracter in your string
print(brand == 'Clever Tech')  # Compare strings and its return Ture or False
print('Tech' in brand)  # Finding words in string
print('tech' not in brand)  # Finding words in string


# 5. Multiline and Formatting Strings

comment = "hello" \
    "this is" \
    "multi line" \
    "string"

name = 'waleed'

email = """ 
hello {},
how are you?
i am good
"""
print(email.format(name))

email2 = f""" 
hello {name},
age {19 + 1}
how are you?
i am good
"""
print(email2)

# 6. Indentation and Keyword


def myfunction():
    name = 'waleed'
    age = 19
