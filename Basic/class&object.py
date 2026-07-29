
#to map with real word scenarion, we started using object in code.
#this is called object oriented programming

#class
class Student:
    name="kunul adel"

#object
s1=Student()
print(s1.name)


#class & instance attributes 
#class.attr 
#object.attr


# __init__ function

"""
s1-এর self হলো s1
s2-এর self হলো s2

তাই প্রত্যেক object নিজের আলাদা name সংরক্ষণ করতে পারে।
self না থাকলে কী হবে?
তাহলে Python বুঝবে না কোন object-এর name সেট করতে হবে এবং TypeError বা NameError দেখা দিতে পারে।
self শুধু Constructor-এ নয়

সব instance method-এর প্রথম parameter হিসেবে self থাকে
"""
class Student1:
    # __init__ function is same as the constructor as like the java
    def __init__(self, userName):
        self.name=userName

s1=Student1("ami")
print(s1.name)

# Method
#Methods are functions that belong to objects.

class MyNam:
    def __init__(self,userName):
        self.name=userName

    def userdata(self):
        print(self.name)


m1=MyNam("shidd")
m2=MyNam("krishna")

m1.userdata()
m2.userdata()


"""Create student class that takes name & marks of 3 subjects as arguments in constructor.
Then create a method to print the average."""

class Student11:
    def __init__(self, userName, marks):
        self.name = userName
        self.mark = marks

    def printDetails(self):
        print(self.name, " ", self.mark, "\n")



s11=Student11("shiddhartha", 88)
s22=Student11("krishna", 89)

s11.printDetails()
s22.printDetails()


#Decorators
"""
প্রোগ্রামিংয়ে (যেমন Python-এ) আপনি যখন একটি সাধারণ ফাংশন তৈরি করেন, 
তখন সেটির মূল কোড না বদলে যদি বাড়তি কোনো কাজ (যেমন: লগিং করা, 
কাজের সময় গণনা করা, বা সিকিউরিটি চেক) যোগ করতে চান, তখন ডেকোরেটর 
ব্যবহার করা হয়।

@staticmethod: কোনো ক্লাস মেথডকে স্ট্যাটিক মেথডে রূপান্তর করে (এটি ক্লাসের ভেতরের কোনো ডেটা পরিবর্তন করতে পারে না)।
@classmethod: মেথডের প্রথম আর্গুমেন্ট হিসেবে অবজেক্টের বদলে সরাসরি ক্লাসকে (cls) পাস করে।
@property: কোনো মেথডকে ভ্যারিয়েবলের মতো (Attribute) অ্যাক্সেস করার সুবিধা দেয়।
"""

class Decorators:

    @staticmethod
    def showDetails():
        print("here i am using decorator ")


d1=Decorators()
d1.showDetails()

"""
Abstraction:
Hiding the implementation details and only showing the essential features to the user


Encapsulation: 
Wrapping data and function into a single unit (object)
"""


#Create Account class with 2 attributes - balance & account no.
##Create methods for debit, credit & printing the balance.
class Account:
    balance:float
    account_no: str

    def accountDetails(self, balance, account_no):
        self.balance=balance
        self.account_no=account_no

    def showAccountDetails(self):
        print("Account no: ", self.account_no, " \nbalance: ", self.balance)

    def debit(self,amount):
        self.balance = self.balance - amount
        print("Debit amount: ",amount , "current balance: ", self.balance)

    def credit(self, amount):
        self.balance = self.balance + amount
        print("credit amount: ", amount, "current balance: ",self.balance)

a1=Account()
a1.accountDetails(23423.23,"043534287")
a1.showAccountDetails()
a1.debit(500.00)
a1.credit(800.22)


