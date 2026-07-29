#The task is to create a file named practice.txt and write the given text into it.
with open("practice.txt","w") as file:
    file.write("Hi everyone\n")
    file.write("we are learning File I/O\n")
    file.write("using Java.\n")
    file.write("I like programming in Java.")

with open("practice.txt","r") as file:
    data=file.read()
    print(data)

print("after modification:\n")

#replace word into the file
new_data= data.replace("Java", "Python")

with open("practice.txt","w") as file:
    file.write(new_data)

with open("practice.txt","r") as file:
    data1=file.read()
    print(data1)

#Search if the word “learning” exists in the file or not.

find_data=data1.find("learning")
print(find_data)

print(data1)
#From a file containing numbers separated by comma, print the count of even numbers.
numbers = data.split(",")
count = 0

for num in numbers:
        if int(num) % 2 == 0:
            count += 1
print(count)