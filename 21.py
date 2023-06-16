        #№1
#def g():
#    b=2
#    d=b*b
#    yield d
#    print("priv")
#    yield b
#j=g()
#print(next(j))
#print(next(j))
        #№2
#def g():
#    a=2
#    print("1 perebor")
#    yield a
#    a*=2
#    print("2 perebor")
#    yield a
#    a/=2
#    print("3 perebor") 
#t=g()
#for i in g():
#    print(i)
        #№3
#def g(x):
#    a,b=1,1
#    for i in range(x):
#        yield a
#        a,b=b,a+b
#n=int(input("Vvedite chislo="))
#h=list(g(x))
#print(h)
#for i in h:
#    print(i)
        #№4
def g():
    a=1
    while True:
        if a>1:
            for i in range(2,a):
                if a%i==0:
                    break
                else:
                    yield a
        a+=1
for i in g():
    print(i)
