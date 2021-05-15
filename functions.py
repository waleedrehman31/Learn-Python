# python functions

# 1. python function with passing an arguments

def greet(name, age=-1):
    print(f"Hello {name} how are you")
    if age >= 0:
        print(f"I know your age is {age}")


greet("waleed", 20)
greet("Hameed", 10)


# 2.  Function with return value
def anAdult(age):
    if age >= 16:
        return True
    else:
        return False


result = anAdult(45)
print(result)


# ! OR

def anAdult(age):
    return age >= 16


result = anAdult(45)
print(result)


def convertGender(gender="unknown"):
    if gender.upper() == "M":
        return "Male"
    elif gender.upper() == "F":
        return "Female"
    else:
        return f"Gender: {gender} is unknown"


print(convertGender("M"))
print(convertGender("F"))
print(convertGender("m"))
print(convertGender("f"))
print(convertGender("Hello Gender"))

#  3. Built in functions and Import Statement

import math

print(math.isqrt(25))

# 4. Modules
# you can find module topic in our_module folder
