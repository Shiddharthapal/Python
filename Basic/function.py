# # Function Without Parameter
# def function1():
#     print("this is without parameter function")
# function1()

# #Function With Parameter
# def function2(a):
#     print("value of a:",a)

# function2(5)


# #Function With Multiple Parameters and return value
# def function3(a,b,c):
#     sum=a+b+c
#     return sum
# print(function3(4,2,7))


# #Function to Find Maximum Number
# def findmax(a,b):
#     if a>b:
#         print("max value is:",a)
#     else:
#         print("max value is:",b)
# findmax(6,5)

"""
funtion decliaretion:
def funtion1(par1, par2,...):
    #some work
    return value

    
 function1(arg1, arg2, ...)   
"""

"""
Some built-in function in python:
print()
len()
range()
type()
"""

# def function22(a: int= 20):
#     print(a)

# function22()

# def funtion33(b: int=2, c:int=45, e:int=12):
#     sum=b+c+e
#     return sum

# print(funtion33())

#recursion-------------------
def rec_func(n):
    if(n==0):
        return 0
    n+=rec_func(n-1)
    return n

print(rec_func(9))


def print_(n):
    print(n, end=" ")
    if n==0:
        return
    print_(n-1)

print_(9)