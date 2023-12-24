# # ##day1

# # # print("aman")
# # # print("aman \n aman \n jain")
# # # print("aman \n \"aman\" \n jain")


# # ##day2
# # # data types in python and variables
# # #list are mutable
# # list1 = [8,3.3,[-4,5],["aman","jain"]]
# # print(list1)


# # ## tuple are immutable
# # tuple1 = (8,3.3,[-4,5],["aman","jain"])
# # print(tuple1)

# # ##dictionary is a key value pair 
# # dict1 = {"aman":"jain","age":20}
# # print(dict1)

# # # python everything is object

# ##day3
# # operator
# print(17//6)
# print(5%3)
# print(2**3)

##typecasting
# a = "aman"
# b = "2"
# c = "3.3"
# print(type(a))
# print(type(b))
# print(type(c))
# print(b+c)


# # user input in python

# a = input("enter the first number")
# print(a)


# b = input("enter the second number : ")
# c = input("enter the third number :  ")
# print(int(b)+int(c))

## strings slicing
# a = "aman jain"
# print(a[0:2])
# print(a[2:6]) # 2 to 5
# print(a[2:])
# print(a[:5])
# print(a[-5:-1]) # it means print(a[len(a)-5:len(a)-1])
# print(a[-5:])
# print(a[:-1])
# print(a[::-1])
#string are immutable
#example 2
# a = "amanjain"
# print(a.upper())
# print(a.lower())
# print(a.replace("a","b"))
# print(a.split(" ")) # it will split the string from the space   and return a list
# print(a.split("a")) # it will split the string from the a   and return a list
# print(a.find("a")) # it will return the index of the first occurence of the a
# print(a.count("a")) # it will return the count of the a in the string
# print(a.isalpha()) # it will return true if the string is alpha else return false
# print(a.isalnum()) # it will return true if the string is alpha numeric else return false
# print(a.isnumeric()) # it will return true if the string is numeric else return false

# print(a.rstrip(2)) # it will remove the space from the right side of the string


## case
# x = 50
# match x:
#     case 1:
#         print("one")
#     case 2:
#         print("two")
#     case 3:
#         print("three")
#     case 4:
#         print("four")
#     case 5:
#         print("five")
#     case _:
#         print("something else")

#functions
# def add(a,b):
#     return a+b
# print(add(2,3))

# def name(fname, mname ="kumar", lname="jain"):
#     print("hello " ,fname,mname,lname)
# name("aman")


# def add(*args):
#     print(args)

# add(1,2,3,4,5,6,7,8,9,10)

# def add(**args):
#     print(args)
# add(a=1,b=2,c=3,d=4,e=5,f=6,g=7,h=8,i=9,j=10)


##list are ordered and mutable
# list1 = [1,2,3,4,5,6,7,8,9,10]
# print(list1)
# print(list1[0])
# list1.append(11)
# list1.insert(0,0)
# list1.remove(0)
# list1.sort()
# list1.reverse()
# list2 = list1.copy() # it will copy the list1 to list2
# list1.extend(list2) # it will extend the list1 with the list2
# print(list1)


# #tuple are ordered and immutable
# tuple1 = (1,2,3,4,5,6,7,8,9,10)
# print(tuple1)
# print(tuple1[0])


##string formating
# fname = "aman"
# lname = "jain"
# print("hello {} {}".format(fname,lname))


# print(f"hello {fname} {lname}")


##doc string
# def add(a,b):
#     """this function will add two number"""
#     return a+b
# a = add().__doc__
# print(a)


## set are unordered and unindexed, no duplicate value
set1 = {"carla",19 , False , 5.9}
print(set1)
set1.add(11)
set1.remove(11)
set1.discard(11)
set1.pop()
