
#set is collection of unorder items (but auto sorted), unique*, immutable(modified)
nums={1,2,3,4,5}
set1={1,2,2,2,2}
set2={7,8,3,4,5,4}
print(nums)
print(set1)
print(set2)

nums.add(10) #add a new value in a set
print(nums)

nums.remove(2) #remove a specefic value from the set
print(nums)

nums.clear() #clear the set
print(nums)

set2.pop() #remove a random value
print(set2)


new_set=set() #create a new set
new_set.add(3)
new_set.add(6)
new_set.add(9)
print(new_set)
print(len(new_set))


union_code=new_set.union(set2) #combine both set and return new
print(union_code)


intersection_set=new_set.intersection(set2)
print(intersection_set)


