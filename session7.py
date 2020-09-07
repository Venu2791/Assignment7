#Q1 Fibbinocci series
import random
checkfib=random.choices([1,3,6,7,4,56,78,99],k=3)
print(checkfib)
fibfilter=filter(lambda x: x in [i+(i-1) for i in range(-1,10000) if i>0 ],checkfib)
list(fibfilter)

#Q2A
a=[1,2,3,4]
b=[4,5,6,8]

def sumiterables(a,b):
    print(list([y for x in zip(b,a) for y in x]))

sumiterables(a,b)

#Q2B
vowels=["a",'e','i','o','u']
name=list("tsai")
[x for x in name if x not in vowels]

#Q2C
numberlist=random.choices(range(-100,100),k=10)
print(numberlist)
[x for x in numberlist if x >0]

#Q2D
import math
numberlist=random.choices(range(-100,100),k=4)
print(numberlist)
[1/(1+math.exp(-x)) for x in numberlist]

#Q4A
import functools
from functools import reduce

a=random.choices(range(1,10),k=5)
print(a)
reduce(lambda x,y: x+y, filter(lambda x: x%2==0,a))

import string
alphabets=list(string.ascii_letters)
name=random.choices(alphabets,k=random.randrange(3,8))
print(name)
print(list([ord(x) for x in name]))
reduce(lambda x,y: x if ord(x)>ord(y) else y,name)