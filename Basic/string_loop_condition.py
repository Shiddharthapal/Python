# char = input("Enter your name:")
# print(char)

# #length
# length=len(char)


# #Slicing
# # str[starting_index:ending_index]

# str="amar_collage"
# print(str[0:4]) #amar
# print(str[3:6]) #r_c
# print(str[:5]) #amar_
# print(str[2:]) #ar_collage

# #slicing using negative indexing
# str="amar_collage"
# print(str[-4:-2])#la


# #String Functions
# str = "i am a coder."
# old='a'
# new='an'
# print(str.endswith("er"))
# print(str.capitalize())
# print(str.replace(old,new))
# print(str.find("coder"))
# print(str.count('a'))

# name="python"

# # this findout the uppercase charecter in the string
# for ch in name:
#     if ch.isupper():
#         print(ch)

# for ch in name:
#     print(ch)


# value=input("ENter the string:")
# for ch in value:
#     print(ch)

# chareacter=input("enter a character:")
# print(chareacter)


# # check the insert character is vowel or not
# ch1=input("Enter a character:")
# if ch1 in 'aeiouAEIOU':
#     print(ch1,"is a vowel")
# else:
#     print(ch1, "is not a vowel")


# #if-elif-else
# mark=78
# if mark<60:
#     print("fail")
# elif mark<70:
#     print("C+")
# elif mark<80:
#     print("A")
# else:
#     print("A+")

# #Array (List) to String
# letters=['p','y','t','h','o','n']
# text="".join(letters)
# print(text)
# #output: python

# letter=['d','j','a','n','g','o']
# text1="  ".join(letter)
# print(text1)
# #output:d  j  a  n  g  o


# #List of Words to String
# word_list=["i","love","my","country"]
# paragraph=" ".join(word_list)
# print(paragraph)

# #String to List (Reverse of join())
# text="python"
# letter2=list(text)
# print(letter2)

# #for loops with else 
# list=[1,2,3,4,5]
# for el in list:
#     print(el)
# else:
#     print("END")

# #range() ->range(start?, stop, step?) - start:0(default), increment:1(Default)
# #step= increment by  step value like(i=0,step=3, 0+3=3)
# for el in range(5):
#     print(el)

# for el in range(2, 6):
#     print(el)

# for el in range(1,7,3):
#     print(el)

# continue, break

# ১. প্রাথমিক কাঠামো তৈরি (Structural Stubbing)
def calculate_metrics():
    pass  # এই ফাংশনের কাজ পরে লেখা হবে

class DataPipeline:
    pass

# ২. এরর বা ভুল এড়িয়ে যাওয়া (Silent Exception Handling)
try:
    with open("config.txt") as file:
        config = file.read()
except FileNotFoundError:
    pass  # ফাইল না পাওয়া গেলেও কোনো এরর দেখাবে না, নীরবে এড়িয়ে যাবে

# ৩. কন্ডিশন ফাকা রাখা (Conditional Placeholder)
status="deactive"
if status == "active":
    process_data()
else:
    pass  # স্ট্যাটাস একটিভ না হলে কোনো কিছু করার প্রয়োজন নেই
