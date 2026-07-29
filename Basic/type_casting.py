# String to Integer
x = "25"
print(int(x))

# Binary to Decimal
binary = "1010"
print(int(binary, 2))

# Octal to Decimal
octal = "17"
print(int(octal, 8))

# Hexadecimal to Decimal
hexa = "A"
print(int(hexa, 16))

##output:
'''
25
10
15
10
'''


#float(y)
x = 25
print(float(x))
y = "15.75"
print(float(y))


#complex(real, imag)
x = complex(5, 3)
print(x)

print(complex(7))


#str(y)
x = 100
print(str(x))
print(type(str(x)))


#tuple(y)
numbers = [10, 20, 30]
result = tuple(numbers)
print(result)
print(type(result))
"""
Output:
(10, 20, 30)
<class 'tuple'>
"""

#list(y)
colors = ("Red", "Green", "Blue")
result = list(colors)
print(result)
print(type(result))

"""
output:
['Red', 'Green', 'Blue']
<class 'list'>
"""


#set(y)
numbers = [1, 2, 2, 3, 3, 4]
result = set(numbers)
print(result)
print(type(result))

"""output:
{1, 2, 3, 4}
<class 'set'>
"""


#dict(y)
data = [
    ("name", "Rahim"),
    ("age", 22),
    ("city", "Dhaka")
]
student = dict(data)
print(student)
print(type(student))

"""
Output:
{'name': 'Rahim', 'age': 22, 'city': 'Dhaka'}
<class 'dict'>
"""

#ord(y)
#Converts a single character to its Unicode (ASCII) value.
print(ord("A"))
print(ord("a"))
print(ord("1"))
print(ord("@"))

"""output:
65
97
49
64
"""

#hex(y), oct(y), bin(y)
print(hex(10))
print(oct(10))
print(hex(100))

"""
output:
0xa
0o12
0x64
"""

#chr() (Reverse of ord())
#converts a Unicode (ASCII) value back to a character.
print(chr(65))
print(chr(97))

"""
output:
A
a
"""



#Dictionary Type Casting

##List of Tuples → Dictionary
#code:
data = [("name", "Rahim"), ("age", 22), ("city", "Dhaka")]
student = dict(data)
print(student)
print(type(student))

#output:{'name': 'Rahim', 'age': 22, 'city': 'Dhaka'}


##Tuple of Tuples → Dictionary
#code:
data = (
    ("name", "Karim"),
    ("age", 25),
    ("department", "CSE")
)
student = dict(data)
print(student)

#output:{'name': 'Karim', 'age': 25, 'department': 'CSE'}


##Two Lists → Dictionary
#code:
keys = ["name", "age", "city"]
values = ["Rahim", 22, "Dhaka"]
student = dict(zip(keys, values))
print(student)

#output:{'name': 'Rahim', 'age': 22, 'city': 'Dhaka'}

# Ordered (Sorting)

## List → Ordered List
#code:
numbers = [5, 2, 8, 1, 4]
ordered = sorted(numbers)
print(ordered)

#output:[1, 2, 4, 5, 8]

## Tuple → Ordered List
#code:
numbers = (8, 2, 6, 1)
ordered = sorted(numbers)
print(ordered)
print(type(ordered))

#output:[1, 2, 6, 8]

##Set → Ordered List
#code:
numbers = {8, 3, 6, 1}
ordered = sorted(numbers)
print(ordered)

# output:[1, 3, 6, 8]


##Dictionary → Ordered by Key
#code:
student = {
    "city": "Dhaka",
    "name": "Rahim",
    "age": 22
}
ordered = dict(sorted(student.items()))
print(ordered)

# output:{'age': 22, 'city': 'Dhaka', 'name': 'Rahim'}


## Dictionary → Ordered by Value
#code:
marks = {
    "Math": 85,
    "English": 70,
    "Physics": 95
}
ordered = dict(sorted(marks.items(), key=lambda item: item[1]))
print(ordered)

# output:{'English': 70, 'Math': 85, 'Physics': 95}

##