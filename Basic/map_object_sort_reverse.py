# #Convert Strings to Integers
# string=input("enter the string:").split()
# number=list(map(int,string))
# print(number)

# #Square Every Number
# number=[2,3,4,5,6]
# square=list(map(lambda x:x*x, number))
# print(number)
# print(square)

# #divided Every Number
# number=[1,2,3,4,5]
# divided1=list(map(lambda x: x/3, number))
# divided2=list(map(lambda x: int(x/3), number))
# print(number)
# print(divided1)
# print(divided2)

# #Object (Class & Object)
# class Student:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# student1=Student("rahim",22)
# print(student1.name)
# print(student1.age)


# #Sorting
# list_=[2,5,1,8,6,9,3,4]

# ##ascending sorting
# list_.sort()
# print(list_)


# ##descending sorting
# list_.sort(reverse=True)
# print(list_)

# ##sorted() Function
# """
# Unlike sort(), sorted() creates a new sorted list and does not change the original.
# """
# list2=[2,5,1,8,6,9,3,4]
# print(sorted(list2))
# print(list2)


# #Reverse -number
# list=[2,4,5,6,1,2]
# list.reverse()
# print(list)


# #Reverse -string
# text="shiddhartha"
# print(text[::-1])

# # Sort Strings
# fruits = ["Banana", "Apple", "Orange", "Oranha"]
# fruits.sort()
# print(fruits)

# fruits.sort(reverse=True)
# print(fruits)


#Sort Dictionary by Value
marks={
    "math":70,
    "english":80,
    "bangla":90
}

sorted_marks=dict(sorted(marks.items(), key=lambda item:item[1]))
print(sorted_marks)



