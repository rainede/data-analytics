myname = input("What is your name?")
print("I am " +myname +", I am glad to meet you!")

#
myname2=input("What is your name?\n")
print("I am " + myname2 +", I am glad to meet you!")

a=1+2
print(a)
a=(1.045*3)/4
print(a)
4**2
4<(2*3)
a = 12 *3.4
a

import math
math.sin(a)

# To be avoided for good practice as
# it involves importing all functions without defining the library they belong to
from math import *
sin(a)

from math import sin

dict ={'name':'William', 'age':25, 'city':'London'}
dict['name']


for key,value in dict.items():
    print(key,value)

list =[1,2,3,4]
list[2]
list[1:3]
list[-1]

items = [1,2,3,4,5]
for item in items:
         item+1

# map(function, list)
# filter(function,list)
# reduce(function,list)
#lambda
#list comprehension

items =[1,2,3,4,5]

def inc(x): return x+1

# use map to replace the for loop
list(map(inc,items))

list(map((lambda x: x+1),items))
