import random
#def f(x):
#    return x*x
#x=int(input("="))
#y=f(x)
#print(y)

#x=int(input())
#f=lambda x: x*x
#print(f(x))

#x=int(input())
#y=int(input())
#f=lambda x,y: x+y
#print(f(x,y))

#x=int(input())
#y=int(input())
#f=lambda x,y:x+y
#z=lambda x,y:x-y
#k=lambda x,y:x*y
#g=lambda x,y:x/y
#print(f(x,y))
#print(z(x,y))
#print(k(x,y))
#print(g(x,y))

#arr=[1,2,3,4,5]
#f=list(map(lambda x:x**2,arr))
#print(f)

#a=[random.randint(0,9) for i in range(10)]
#f=list(map(lambda x: x**2,a))
#print(f)

#def f(i):
#    if i%2==0:
#        return 1
#    else:
#        return 0
#arr=[random.randint(0,15)
#    for i in range(10)]
#y=filter(f,arr)
#print(list(y))

print(list(filter(lambda x: x%2==0,[random.randint(0,15) for i in range(10)])))
