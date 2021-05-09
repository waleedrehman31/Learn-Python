# ============ Data Structures ============

# 1. Lists

numbers = [1, 2, 3, 4, 0, -1, -20]
# numbers = [1, 2, 3, 4, -1, 0, ['A', 'B']]

print(type(numbers))
print(numbers[0])
print(numbers[1])
print(numbers[2])
print(numbers[3])
print(numbers[4])
print(numbers[5])
print(numbers[6])
print(numbers[6][0])
print(numbers[6][1])


# 2.   Useful List methods

numbers.sort()
numbers.reverse()
numbers.append(2000)
print(len(numbers))
numbers.clear()
print(4 in numbers)
print(5 not in numbers)
print(numbers)


# 3.   Deleting Items from lists

numbers.remove(1)  # it remove only first instance
numbers.pop()  # pop() removes the last item in list i.e -20
numbers.pop()  # pop() removes the last item in list i.e -10
# it is also delete number but using specific index and the range is 0 to 3
del numbers[0:3]
print(numbers)

# 4. Sets
'''
in list duplication are not allowed but in list you can dublicate number as you can. In sets we use curly brackets "{}" instand of suqare brackerts "[]". And sets have same modules that list have. Sets are unordered 
'''
numbersLists = [1, 1]
numbersSets = {1, 1}
lettersSets = {'A', 'A', 'B', 'C', 'C'}
print(numbersLists)
print(numbersSets)
print(lettersSets)

# 5. Set Union Intersection and Difference
'''
| = this symbol is called union. it combine every thing and combine every thing
& = this symbol is intersection. it output the same element in two sets
- = this symbol is used for difference in sets. it remove same element in set and show remaining elements
'''
lettersA = {'A', 'B', 'C', 'D'}
lettersB = {'A', 'E', 'F'}
union = lettersA | lettersB
intersection = lettersA & lettersB
difference = lettersA - lettersB
print(f"Union = {union}")
print(f"Intersection = {intersection}")
print(f"Difference = {difference}")

# 6.   Dictionaries
'''
The dictionary starts with curly {} brackets and inside these brackets the data is
 "Keys: "Values". and the keys have been unique. it also have same module as sets and lists have
'''
person = {
    "name": "Waleed ur Rehman",
    "age": 19,
    "address": "PK"
}
print(person["name"])
print(person["age"])
print(person["address"])
print(person.keys())
print(person.values())
person.clear()
print(person.get("age"))
person["age"] = 100
print(person)
