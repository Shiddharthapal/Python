#list
##how to pick number from list
arr=[1, 2, 3, 4, 5]

#length
length=len(arr)
print(length)




number=arr[2]
print(number)
print(arr[4])
print(type(arr))

##how ro insert
arr.append(6)
print(arr)

##python has a built-in array module
from array import array
arr2=array('i',[1,2,3,4,5,6])

print(arr2)

arr3=array('i',[4,2,6,4,1,9])
print(arr3[4])


arr2.append(9)
arr3.append(7)

print(arr2)
print(arr3)

##Empty array
empty_arr1=[]
empty_arr2=array('i')

print(empty_arr1)
print(empty_arr2)


## input from user
input_arr=[]
for i in range(5):
    num=int(input("Enter a number:"))
    input_arr.append(num)

print(input_arr)

#List Slicing
marks=[23,43,56,21,78,96,35]
print(marks[2:5]) #56,21,78
print(marks[:4]) #23,43,46,21
print(marks[3:]) #21,78,96,35
print(marks[-3:-1]) #78,96


list = [2, 1, 3]

list.append(4) #adds one element at the end [2, 1, 3, 4]
list.sort( ) #sorts in ascending order [1, 2, 3]
list.sort( reverse=True ) #sorts in descending order [3, 2, 1]
list.reverse( ) #reverses list [3, 1, 2]
list.insert( 3,6) # list.insert( idx, el ) insert element at index [2,1,3,6]

list1=[2,1,3,1]
list.remove(1) #removes first occurrence of element [2,3,1]
list.pop(2) #list.pop( idx ) - removes element at idx: [2,1,3,1] to [2,1,1]


##tuple:

#A built-in data type that lets us create immutable sequences of values.
#tuple method
tup=(3,1,4,2,4,1,4)
tup.index(1) #returns index of first occurrence tup.index(1) is 1
tup.count(4) ##counts total occurrences tup.count(4) is 3

