#Q1 Fibbinocci series
import random
checkfib=random.choices([1,3,6,7,4,56,78,99],k=3)
print(checkfib)
fibfilter=filter(lambda x: x in [i+(i-1) for i in range(-1,10000) if i>0 ],checkfib)
list(fibfilter)

#Q2A
#Q2A
a=random.choices(range(0,100),k=4)
b=random.choices(range(0,100),k=4)
print(a)
print(b)
[x+y for x,y in zip(a,b) if x%2==0 and y%2!=0 ]

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

#Q2E
import string
alphabets=list(string.ascii_letters)
name=random.choices(alphabets,k=random.randrange(3,8))
print("".join(name))
#print(list([ord(x) for x in name]))
print("".join(list([chr(ord(x)+5) for x in name])))

#Q4A
import functools
from functools import reduce

a=random.choices(range(1,10),k=5)
print(a)
reduce(lambda x,y: x+y, filter(lambda x: x%2==0,a))

#Q4B
import string
alphabets=list(string.ascii_letters)
name=random.choices(alphabets,k=random.randrange(3,8))
print(name)
print(list([ord(x) for x in name]))
reduce(lambda x,y: x if ord(x)>ord(y) else y,name)

#Q4C
a=random.choices(range(0,100),k=8)
print(a)
reduce(lambda x,y: x+y,filter(lambda x: x if a.index(x)%2==0 else 0,a))

#Q5
import string
["KA"+str(random.choice(range(10,99)))+"".join(random.choices(string.ascii_uppercase,k=random.randint(0,3)))+str(random.choice(range(1000,9999))) for i in range(15)]

#Q6
from functools import partial
def numberplate(state,distnum,rto,No):
    numberplate=state+str(distnum)+rto+str(No)
    return numberplate

f=partial(numberplate,distnum=random.choice(range(10,99)),rto="".join(random.choices(string.ascii_uppercase,k=random.randint(0,3))),No=random.choice(range(1000,9999)))
f("DL")
