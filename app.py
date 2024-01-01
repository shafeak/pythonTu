
#Variables
x= 5
y= "john"
print (x)
print(y)         #make identation reference here

#variables

print ("hello world")
character_name = 'George'
character_age = '70'
print ("there was a man named"  + character_name +"")
print ("he was" "character_age")
print ("he really liked the name " + character_name +"")
print ("but")
print ("he didnt like being" + character_age +"")


##################################################
#Strings
a= "hello world"
print (a)

print (a[2])
print (a [2:5])

print(len(a))
print (a.upper())
print (a.replace("hello", "happy new year"))

for x in "hello world":
    print(x)





#Taking input from users
name = input ("enter your name:")
age = input ("enter your age:")
print( "hello "  + name + " you are "+age)
#############

#Building a calculator
num1= input("enter a number:")
num2= input("enter another number:")
result= num1 + num2
print(result)


num1= input("enter a number:")
num2= input("enter another number:")
result= int(num1) + int(num2)
print(result)


num1= input("enter a number:")
num2= input("enter another number:")
result= float(num1) + float(num2)
print(result)
 #####################

#lists
mylist =["ali","hamid","ali","john","muller"]
mylist1= [1,2,3,4,5]
mylist2= [True, False, True ]
print(mylist)                                     #datatypes
print(mylist1)
print(mylist2)

#list constructor
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

mylist.append("sara")      #add at end of list
print(mylist)
mylist.insert(1,"rebica")  #insert at specific position
mylist.remove("ali")

#loop through thelist
mylist =["ali","hamid","ali","john","muller"]
for x in mylist:
    print (x)


Print (x)print(mylist.index("hamid"))   #tells position or index of an item in list
print(mylist.count("john"))
print(mylist.sort())           #sorts in accending order

my_number= [1,2,3,4,5]
(my_number.reverse())
print(my_number)


#Tuples
coordinates= (4,5,5)
 print(coordinates)
 print(coordinates[1])      #access at specific index

#tuple with str.int,bolean
tuple1 = ("abc", 34, True, 40, "male")
print (tuple1)

#functions
def my_function():
  print("Hello from a function")
  my_function()

  def say_hi(name,age):
      print("hello " + name +", you are "+ age)

    say_hi("Mike","35")
    say_hi("Steve","70")


#If else statements
is_male= True #boolean variable
is_tall= True

 if is_male and is_tall:
     print("you are a tall male")
 elif is_male and not(is_tall):
     Print("you are a short male")
 elif not(is_male) and is_tall:
     print("you ae not male but are tall")
 else:
     print("you are not a male and not tall")


 #Calculator
num1 = float(input("enter frist number:"))
op = input("enter operator:")
num2= float(input("enter second number:"))

 if op == "+":
     print(num1 + num2)
 elif op == "-":
     print(num1-num2)
 elif op =="/":
     print(num1 / num2)
 elif op =="*":
     print(num1 * num2)
 else:
     print("invalid operator")


     #dictionaries
 monthConversions = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december",

}

print(monthConversions["nov"])


x= monthConversions.keys()
print(x)
monthConversions["sem"]="semester"
print(x)



#loop through dictionaries
 monthConversions = {
    "jan": "january",
    "feb": "february",
    "mar": "march",
    "apr": "april",
    "may": "may",
    "jun": "june",
    "jul": "july",
    "aug": "august",
    "sep": "september",
    "oct": "october",
    "nov": "november",
    "dec": "december",

}
for x in monthConversions:
    print(x)

#remove itemes from dictionaries
monthConversions.pop("dec")
print(monthConversions)