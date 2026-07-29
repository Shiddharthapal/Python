# #Count Characters in a String

# string=input("ENter a string:")
# count=0
# for ch in string:
#     count+=1
# print("The number of characters in the string is:",count)

# #Print Character with Index
# value="oylou"
# for i in range(len(value)):
#     print(value[i],i)


# #Count Vowels
# word=input()
# count=0
# for i in range(len(word)):
#     if(word[i] in 'aeiouAEIOU'):
#         count+=1

# print("The number of vowels in the string is:",count)


# #Reverse a String Using for Loop
# word=input("Enter a word:")
# reverse=""
# for ch in word:
#     reverse=ch+reverse
# print("The reverse of the string is:",reverse)

# #this findout the uppercase charecter in the string
# word12=input("Enter a word:")
# for ch in word12:
#     if ch.isupper():
#         print(ch)


# #Write a Program to input 2 numbers & print their sum.
# a=int(input("Enter the value of a:"))
# b=int(input("Enter the value of b:"))
# print("the sum=",a+b)


# #WAP to find the greatest of 3 numbers entered by the user
# #For Space-Separated Inputs
# number=[int(x) for x in input("enter numbers:").split()]
# number.sort(reverse=True)
# print(number[0],number[1],number[2])


"""
Store following word meanings in a python dictionary :
table : “a piece of furniture”, “list of facts & figures”
cat : “a small animal”
"""
dictonary={
    "table" : {"a piece of furniture", "list of facts & figures"},
    "cat":"a small animal"
}
print(dictonary)



"""
You are given a list of subjects for students. Assume one classroom is required for 1
subject. How many classrooms are needed by all students.

”python”,“java”,“C++”,“python”,“javascript”,“java”,“python”,“java”,“C++”,“C”
"""

set1={"python","java","C++","python","javascript","java","python","java","C++","C"}
print("number of room:",len(set1))


# """WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with
# an empty dictionary & add one by one. Use subject name as key & marks as value."""

# dictionary={}
# for i in range(3):
#     key=input("enter the subject name:")
#     value=input("enter the marks for this subject:")
#     dictionary[key]=value

# print(dictionary)



# """
# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)
# """

# new_set=set()
# new_set.add("9")
# new_set.add("9.0")
# print(new_set)

# #Print numbers from 100 to 1.
# for num in range(100,0, -1):
#     print(num)


# # WAP to find the sum of first n numbers. (using while)

# n=10
# sum=0
# count=0
# while count<n:
#     sum+=count
#     count+=1

# print (sum)


# #WAF to print the length of a list. ( list is the parameter)
# def tempFunc(lists:list):
#     print(lists)
# tempFunc([1,2,3,4,5])


# #WAF to print the elements of a list in a single line. ( list is the parameter)
# def printSingleLine(tempList:list):
#     for item in tempList:
#         print(item, end=" ")
# printSingleLine([2,1,4,1,4])


# #WAF to find the factorial of n. (n is the parameter)
# def factorial(n:int):
#     sum=1
#     for i in range(1, n+1):
#         sum*=i
#     return sum
# print(factorial(6))


# #WAF to convert USD to INR. with two decimal point 
# def inrConverter(dollar):
#     inr=dollar*75.32
#     return inr
# print("USD to Inner:", f"{inrConverter(10):.2f}")