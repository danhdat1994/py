import random
roll =random.randint(1, 6)
print(roll)
c=int(input('input value\n'))
a=c//10
b=c%10
if not a>b and a<b or a<b:
    print('top > bot')
else:
    print('top < bot')
print(str(a)+"\n"+str(b)+"\n"+str(c))

list=[]
list.append('1')
list.append('2')
list.append('3')
a =range(7)