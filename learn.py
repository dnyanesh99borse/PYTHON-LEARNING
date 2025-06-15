#sum two numbers using input function

# a = int(input("enter a value of a: "))

# b = int(input("enter a value of b: "))

# print(a + b)


# a = 34 
# b = 5 
# print("Remainder when a is divided by b is: ", a % b)


# user_input = input("Enter something: ")
# print(f"You entered: {user_input}")


# a = int(input("Enter number 1: "))
# b = int(input("enter the number b:"))

# print("the average of the two numbers is: ", (a + b) / 2)

# a = int(input("enter your number: "))

# print("the square of the number is: ",a**2)





# name = "dnyanesh"

# print(len(name))   

# print(name[0:3])
# print(name[1:3])
# print(name[0:5]) #it will print the letters from 0 to 4
# print(name[-4:-1]) #here this are the negativ indexes
# print(name[4:7]) #here this are corresponding positive indexes

# #so that we can convert the negative index into corresponding positive indexes

# print(name[:4]) #it is equall to the starting from 0 to 4 indexing
# print(name[1:]) #it is equall to the starting from 1 to index minus 1
# print(name[1:8])


#SLICING WITH SKIP VALUE

# b = "abcdefghijkmlnopqrstuvwxyz"

# print([b[1:9:4]]) #here the output is "bf" cause, first of all it will 
#                   #display the elements from 1 to 8 here that is: abcdefghi
#                   #and from this elements it will display the element at the fourth position starting from 1 here
#                   #from that elements that is b. and thus it becames: "bf"

# print([b[1:10:4]]) #(abcdefghij) : starting from 1 => bfj



# # SOME IMPORTANT FUNCTIONS OF THE STRINGS: 
# name = "i am a successfull independent billionaire"
# print(len(name))
# print(name.endswith("re"))
# print(name.endswith("xyz"))
# print(name.endswith("re", 0, 9)) #here it will check the string from
#                                  #0 to 9 index and it will return true if the string ends with "re"

# print(name.startswith("ha"))
# print(name.startswith("bi"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.title())
# print(name.swapcase()) #it will swap the case of the string
# print(name.count("i")) #it will count the number of the "i" in the string
# print(name.find("i")) #it will return the index of the first occurrence of the "i
# print(name.rfind("i")) #it will return the index of the last occurrence of the "
# print(name.replace("successfull", "most_successfull")) #it will replace the "i" with "a
# print(name.split()) #it will split the string into the list of the words
# print(name.split("i")) #it will split the string into the list of the words at the
# #index of the "i" in the string
# print(name.split("i", 1)) #it will split the string into the list of the
# #words at the index of the "i" in the string and it will stop after the first

# s = "    billionaire    "
# name = "dnyanesh"

# print(s.isalpha())    # Output: False
# print(s.isdigit())    # Output: False
# print(s.isalnum())    # Output: True

# print(s.strip())   # Output: Hello, World!
# print(s.lstrip())  # Output: Hello, World!   
# print(s.rstrip())  # Output:    Hello, World!

# print(f"hey i am {name} and i am a successfull independent {s}")


#================ESCAPE SEQUENCE CHARACTER
# a = " Dnyaneshwar is a\n successfull \n independent\n Billionaire \n he is also a G.O.A.T."

# b = "Dnyanesh is a \"billionaire\"\n"
# c = 'Dnyanesh is a \'billionaire\''
# print(a,b,c)

# a = "I \u2764 YOU \U0001F600 \n"
# # b = "I love you Queen \N{smiling face}"

# print(a)



 
# letter = '''Dear <|Name|>,
#             you finally became a 
#             <|aim|>'''

# print(letter.replace("<|Name|>","dnyaneshwar").replace("<|aim|>", "successfull independent \n billionaire"))

# name = "i  am  a  billionaire" #string containing double space

# print(name.replace("  "," "))
#REMEBER HERE STRINGS ARE IMMUTABLE THAT THE FUNCTIONED STRING WILL NOT CHANGE IN ORIGINAL STRING


#================LISTS=================

# friends = ["Apple","Orange",5,345.06,False,"Aakash","DOLLAR"]

# print(friends)
# print(type(friends))
# print(friends[6])
# friends[6] = "Billion"
# print(friends[6])
# print(friends[1:4])

# #==different methods on lists==
# friends.append("rupees")
# print(friends)

# friends.extend(["mom","dad","sisters","family"])
# print(friends)

# friends.insert(2,'SACRIFICE')
# print(friends)

# friends.remove(5) #will remove first occurence
# print(friends)

# removed_item = friends.pop(3)
# print(removed_item)
# print(friends)

# print(friends.index("mom"))
# print(friends.index("mom"))
# print(friends.index("dad"))
# print(friends.index("sisters"))

# print(friends.count(5))

# friends.sort()
# print(friends)

# friends.sort(reverse=True)
# print(friends)

# friends.reverse()
# print(friends) #return value


#String is anoter data type which can only store the similar datatype and is immutable

#list is another set of heterogenous datatype and which is mutable

#-------------TUPLE DATATYPE-------------------------
#tuple is another  heterogenous datatype like a list just the tuple is immutable
#means you can not never change the tuple. it a collection of fixed data type
#for any method it will return it in new tuple like string
# a = (1,2,4,5,2,4)
# print(type(a))

# print(a.count(2))

# i=a.index(4)
# print(i)

# my_tup = (1,2,3,4,5)
# print(2 in my_tup)
# print(5 in my_tup)

# print(a+my_tup)
# print(2*my_tup) #it will double the elements of tuple

# print(my_tup[1:4])

# a,b,c,d,e = my_tup
# print(a,b,c,d,e)

# fruits = []
# f1=input("Enter fruit name: ")
# fruits.append(f1)
# f2=input("Enter fruit name: ")
# fruits.append(f2)
# f3=input("Enter fruit name: ")
# fruits.append(f3)
# f4=input("Enter fruit name: ")
# fruits.append(f4)
# f5=input("Enter fruit name: ")
# fruits.append(f5)
# print(fruits)


# Students = []
# s1= int(input("Enter marks here: "))
# Students.append(s1)
# s2= int(input("Enter marks here: "))
# Students.append(s2)
# s3= int(input("Enter marks here: "))
# Students.append(s3)
# s4= int(input("Enter marks here: "))
# Students.append(s4)
# s5= int(input("Enter marks here: "))
# Students.append(s5)
# s6= int(input("Enter marks here: "))
# Students.append(s6)
# Students.sort()
# print(Students)
# Students[2] = "billion"
# print(Students) #it will replace the 3rd element with "billion" and rest


# a,b,c,d,e,f = Students
# print(a,b,c,d,e,f)

# Stu_tup = (a,b,c,d,e)
# print(Stu_tup) #it will print the tuple of the elements of list

# s = [1,2,3,4,5]
# print(sum(s))
# # print(sum(Stu_tup))

#------------DICTIONAIRY AND SETS----------------------
#Dictionary is another datatypes whose elements has the key & values is mutuable and can't have duplicate entries
# key is unique and value can be duplicate

# marks = {
#     "John": 90,
#     "Alice": 85,
#     "Bob": 95,
#     "John": 55,#it will replace the previous value of John
#     0: "harry"
# }

# print(marks)
# print(marks["John"]) #it will print the value of John
#-------------------method of the DICTIONART------------------------
# print(marks.keys())
# print(marks.values())
# marks.update({"Harry":99,"Renuka":100}) #jo element present hai use update or nahi hai use add kar dega
# print(marks)

# print(marks.get("harry")) #it returns a none
# print(marks["harry"]) #it will give error because harry is not present in

#METHODS IN DICTIONARY
#1.pop() - it will remove the key and return the value
#2.popitem() - it will remove the last item and return the key and value
#3.clear() - it will remove all the items from the dictionary
#4.copy() - it will return a copy of the dictionary
#5.get() - it will return the value of the key if key is present otherwise it will
#6.items() - it will return the key and value as tuple
#7.keys() - it will return the keys of the dictionary
#8.values() - it will return the values of the dictionary
#9.update() - it will update the dictionary with the items from another dictionary
#10.setdefault() - it will return the value of the key if key is present otherwise it will

# marks = {
#     "John": 90,
#     "Alice": 85,
#     "Bob": 95,
#     "John": 55,#it will replace the previous value of John
#     0: "harry"
# }

# print(marks)
# print(marks.pop("John"))
# print(marks)

# print(marks.popitem())
# print(marks)
# # print(marks.popitem())
# # print(marks.copy())
# # print(marks.get("harry"))
# # print(marks.setdefault("harry",100))

# my_dict = {"a": 1, "b": 2}
# print("a" in my_dict)  # Output: True
# print("c" not in my_dict)  # Output: True

# my_dict = {"a": 1, "b": 2}
# print(len(my_dict))  # Output: 2

#d = {} IT CREATES AN EMPTY DICTIOARY
#---------------------SETS--------------------------
#sets is a collection of well-defined objects
#it holfs all the conditions of sets
#set can be write as s = {1,2,3,4,5}
# e = set() #Dont use s = {} as it will create an empty dictionary
# unordered
#cannot change existing elements
#can add new elements
#can remove existing elements

#---------------------SETS METHODS--------------------------

# s = {1,2,3,4,5}
# print(type(s))

# s.remove(1)
# print(s)

# s.pop()
# print(s)

# # s.clear()
# # print(s)

# #-----union method & intersection-------
# s1 = {1,2,3,4,5}
# s2 = {4,5,6,7,8}

# print(s1.union(s2))
# print(s1.intersection(s2))

# print(s1 - s2)

# s.update([4,5,6,7,8])
# print(s)

# s.remove(4)
# print(s)

# my_set = {1, 2, 3}
# my_set.discard(4)  # No error even if 4 is not in the set
# # Removes a specific element from the set. Does not raise an error if the element is not found.
# print(my_set)  # Output: {1, 2, 3}

# print(s.pop())


# set1 = {1, 2, 3}
# set2 = {2, 3, 4}
# print(set1.symmetric_difference(set2))  # Output: {1, 4}

# set1 = {1, 2}
# set2 = {1, 2, 3}
# print(set1.issubset(set2))  # Output: True

# set1 = {1, 2, 3}
# set2 = {1, 2}
# print(set1.issuperset(set2))  # Output: True


# set1 = {1, 2}
# set2 = {3, 4}
# print(set1.isdisjoint(set2))  # Output: True

# #------------------sets using operstors------------------
# print({1, 2} | {3, 4})  # Output: {1, 2, 3, 4}

# print({1, 2, 3} & {2, 3, 4})  # Output: {2, 3}

# print({1,2,3} - {2,3}) #difference of a - b

# print({2,3} - {1,2,3}) #difference of b - a

# print({1,2,3} ^ {2,3,4}) #disjoint


#problem one to make a simple dictionary
# my_dic = {
#     "water": "pani",
#     "apple": "seb",
#     "dog": "kutta",
#     "cat": "billi"
# }

# word = input("Enter a word you want to search: ")
# print(my_dic[word])

# c = [1,2,3,4,5] #----------LIST
# print(type(c))

# a = (1,2,4,5,2,4) #----------TUPPLE
# print(type(a))

# c = {"a":1,"b":2,"c":3,"d":5} #----------DICTIONARY
# print(type(c))

# b = {1,2,4,5,2,4} #----------SETS
# print(type(b))

#problem2
# s = set()
# n = input("Enter a number:")
# s.add(int(n))
# n = input("Enter a number: ")
# s.add(int(n))
# n = input("Enter a number: ")
# s.add(int(n))
# n = input("Enter a number: ")
# s.add(int(n))
# n = input("Enter a number: ")
# s.add(int(n))
# n = input("Enter a number: ")
# s.add(int(n))
# print(s)


# s = set()
# s.add(18)
# s.add('18')
# print(s)

# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20')
# print(s)

# s = {}
# print(type(s))

# d = {}
# name = input("Enter friends name: ")
# lang = input("Enter a language name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter a language name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter a language name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter a language name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter a language name: ")
# d.update({name: lang})
# print(d)

#REMEBER HOW THE VALUE CHANGES AS UPDATION IF FIRST THE VALUE IS DIFFERENT AND YOU ARE ASSIGNING
#THE ANOTHER VALUE TO THAT KEY THEN IT WILL CHANGE

# d = {}
# name = input("Enter friends name: ")
# lang = input("Enter a language name: ")
# d.update({name: lang})
# name = input("Enter friends name: ")
# lang = input("Enter a language name: ")
# d.update({name: lang})
# print(d)

# PS C:\Users\LENOVO\Desktop\TRANSFORM JYTSU\skill sets\PYTHON> python learn.py
# Enter friends name: aman
# Enter a language name: c
# Enter friends name: aman
# Enter a language name: java
# {'aman': 'java'}
# PS C:\Users\LENOVO\Desktop\TRANSFORM JYTSU\

#in dictionary values might be same but not the keys..and dont allows duplicates.


#BY DEFAULT PYTHON ACCEPTS THE INPUT AS STRING

#================IF ELIF LADDER=====================
# a = int(int(input("Enter your age: ")))

# if(a>=18):
#     print("You are adult")
# elif(a<0):
#     print("Your are entering invalid age")
# elif(a == 0):
#     print("yor are entering 0 which can't age")
# else:
#     print("You are not adult")

# print("End of program") #this is the line outside the if else .

#remeber if anyone of the condition become true it will stop


#===============in keyword=================
# p1 = "how"
# p2 = "are"
# p3 = "you"
# message = input("Enter your comment: ")
# if(p1 in message or p2 in message or p3 in message):
#     print("This is a spam")
# else:
#     print("This is not a spam")


# post = input("Enter the post: ")
# if ("harry" in post.lower()): #this lower function for post will convert 
#     #any type of hARry input in lower case and then willcheck condition
#     print("This post is talking about harry")
# else:
#     print("This post is not talking about harry")

# list = [2,"harry",True,"hi","Rohan"]
# i = 0
# while(i < len(list)):
#     print(list[i])
#     i += 1.


#=================WE CAN USE FOR LOOP WITH ELSE=================
# name = "dnyanesh"
# for i in name:
#     print(i) #this will print each character of the name
# else: 
#     print("This is else block") #this will print if the loop is not executed


#=================BREAK===========================
# for i in range(100):
#     if(i == 34):
#         break
#     print(i)
#HERE IT WILL DIRECT STOPS AT THIS CONDITON AND WILL NOT CONTINUE
#IT INSTRUCT TO EXIT THE LOOP NOW
#=======================CONTINUE=========================
# for i in range(100):
#     if(i == 34):
#         continue
#     print(i)
#HERE IT WILL SKIPS THIS CONDITON AND WILL CONTINUE FROM NEXT ITERATION



#================================FULL PYTHON MASTER COURSE FROM ZERO TO HERO====================================#
#============DATATYPES===============

# a = 11.80
# x = 100
# y = "hello"
# z = 3 + 5.j
# print(a,x,y,z)

# num = input("enter a number: ")
# print(num)


#-------------------problem statement-------------------
# import math
# num = int(input("Enter a number: "))
# square = num ** 2
# print("Square of the number is: ",square)
# cube = num ** 3
# print("Cube of the number is: ",cube)
# sqroot = math.sqrt(num)
# print("Square root of the number is: ",sqroot)


# n1 = int(input("enter a num1: "))
# n2 = int(input("Enter a num2: "))
# n3 = int(input("Enter a num3: "))
# average = (n1+n2+n3)/3
# print("Average of the 3 numbers is: ",average)


# base = int(input("Enter the base of the triangle: "))
# height = int(input("Enter the height of the triangle: "))
# area = 0.5*base*height
# print("area of the right angle triangle is: ",area)


# p = int(input("Enter a amount: "))
# r = int(input("Enter a rate: "))
# t = int(input("Enter a time period: "))
# si = (p*r*t)/100
# print("Simple interest is: ",si)


# c = int(input("Enter a Temperature in Celcius: "))
# f = (c * (9/5) + 32)
# print(f"the farhenheit of {c} is: ",f)

# import math
# x1 = int(input("Enter the value of x1: "))
# x2 = int(input("Enter the value of x2: "))
# y1 = int(input("Enter the value of y1: "))
# y2 = int(input("Enter the value of y2: "))
# ed = math.sqrt((x1-y1)**2 + (x2-y2)**2)
# print("The euclidean distance bet. two points are: ",ed)

# a = 10
# b = 20
# temp = 0
# print(a,b)
# temp = a
# a = b
# b = temp
# print(a,b)

# a,b = b,a
# print("a & b after swapping using comma: ",a,b)

# a = a^b
# b = a^b
# a = a^b
# print(a,b)


# import math
# a = float(input("Enter the coeffiecient a: "))
# b = float(input("Enter a coefficient b: "))
# c = float(input("Enter a coefficient c: "))
# if a == 0:
#     print("This is not a quadratic equation (a cannot be zero)")
# else:
#     d = b**2 - 4*a*c
    
#     if d > 0:
#         root1 = (-b + math.sqrt(d))/(2*a)
#         root2 = (-b + math.sqrt(d))/(2*a)
#         print("the roots are real and distinct: ")
#         print("Root 1 = ",root1)
#         print("Root 2 = ",root2)
#     elif d == 0:
#         root = -b / (2*a)
#         print("The roots are real and equal:")
#         print("Root 1 = Root 2 =", root)
#     else:
#         real_part = -b / (2*a)
#         imag_part = math.sqrt(-d) / (2*a)
#         print("The roots are complex:")
#         print(f"Root 1 = {real_part} + {imag_part}i")
#         print(f"Root 2 = {real_part} - {imag_part}i")

# s1 = float(input("Enter side 1: "))
# s2 = float(input("Enter side 2: "))
# s3 = float(input("Enter side 3: "))
# if s1 == s2 == s3:
#     print("This is Equilateral Triangle")
# elif s1 == s2 or s2 == s3 or s3 == s1:
#     print("The triangle is Isoceles triangle")
# else:
#     print("The triangle is a Scalen triangle")



#----------STRINGS AND CONDITIONAL STATEMENTS----------
#String is a data type that stores a sequence of characters

# str1 = "this is a string"
# str2 = 'this is also a string'
# str3 = '''this is also a valid string''' 
#this triple qotes we use in case when we wants to use single apostropee so thus we use 
#triple qote


#ESCAPE SEQUENCE CHARACTERS#
#this are the special type of characters we use for the particular tasks like
# whenever we want to provide space in betn to diff. sentences and all then we use 
# these sequence charcters

# and thus to print the next sentence on the next line we use the escape sequence character 
# '\n'

# str1 = "this is a string. \nwe are creating it in python"
# print(str1)

# str2 = "this is a string. \twe are creating it in python"
# print(str1)


#----------OPERATIONS ON STRINGS-----------------
# #1) concatination
# str1 = "i am a "
# str2 = "billionaire"
# print(str1+str2)

# str1 = "i am a "
# str2 = "billionaire"
# fstr = str1+str2
# print(fstr)


# #2) Length of string
# print(len(str1))
# print(len(str2))
# print(len(fstr))
# #in python any letter,number,digit,spaces,specialchar. also counts during length


#INDEXING
#In pyton we use the idexing for accessing elemens and here also indexing start from 0.
#we cannot manipulate strings using indexing.
# str1 = "billionaire  "
# print(str1[3])
# print(str1[12])


#------------------SLICING IN PYTHON: VIMP FOR MACHINE LEARNING-----------------
#slicing allows accessing parts of a string. 
#ending index is not included in the slicing means it will stop on last index and dont add 
#....add that last index element in our sliced part. 
#like in below example it included the l of index 2 but didn't included o of index 5.

# str1 = "billionaire"
# print(str1[2:5])

# # str2 = "i am a billionaire"
# # print(str2[7:18])

# # str2 = "i am a billionaire"
# # print(str2[7:len(str2)])

# # str3 = "billionaire"
# # print(str3[0:18])

# # str3 = "billionaire"
# # print(str3[:18])

# # str3 = "billionaire"
# # print(str3[1:])

# # str3 = "billionaire"
# # print(str3[0:])

# # str3 = "billionaire"
# # print(str3[:])

# #---------------backward indexing in python----------------
# #we can also access string elements in reverse order using negative indexing.
# #negative indexing starts from -1 and goes backwards to -n where n is the length of th
# #string.

# str = "Apple"
# print(str[-3:-1])

# str = "Apple"
# print(str[-3:])

# #--------string functions-----------
# str = "I am a billionaire"
# print(str.endswith("re")) #returns true if string ends with substr

# str = "I am a billionaire"
# print(str.endswith("xyz")) #returns true if string ends with substr

# str = "billionaire"
# print(str.capitalize()) #capitalizes 1st char
# print(str.capitalize()) 

# #but like the below execution we can change in our original string. 
# str = str.capitalize()
# print()
# print(str)
# #capitalize creates a new string and not changes in old string

# # print(str.replace(old, new)) #replaces all occurences of old with new
# str = "i am a billionaire"
# print(str.replace("b","M"))

# str = "i am a billionaire"
# print(str.replace("billionaire","Trillionaire"))


# print(str.find(word)) #returns 1st index of 1st occurence"
# str = "i am a billionaire"
# print(str.find("i"))

# print(str.find("a"))

# print(str.find("am"))

# print(str.count("am")) #counts the occurences of substr in string.
# str = ("i i i am a billionaire billionaire")
# print(str.count("i"))

# print(str.count("billionaire"))


#practice question:
#WAP TO INPUT USER'S FIRST NAME AND PRINT ITS LENGth

# name = input("enter your first name: ")
# print(len(name))

#WAP to find the occurence of "$"
# str = "I am a billionaire $$$"
# print(str.count("$"))

#--------CONDITIONAL STATEMENTS--------------
#IF-ELIF-ELSE:
age = 21
if age >= 18:
    print("you are eligible to voteL")
else:
    print("you are not eligible to vote")








