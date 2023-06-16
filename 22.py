    #1
# def den():
#     b=2
#     a=b*b
#     yield a
# t=den()
# print(next(t))
    #2
# def gen():
#     x=2
#     print("per pereb")
#     yield x
#     x*=2
#     print("vtor pereb")
#     yield x
#     x/=2
#     print("tr pereb")
#     yield x
# t=gen()
# #print(next(t))
# for j in gen():
#     print(j)
    #3
# def gen():
#     a,b=1,1
#     for i in range(n):
#         yield a
#         a,b=b,a+b
# n=int(input("v. ch"))
# t=list(gen())
# print(t)
# for c in t: 
#     print(c)
    #4
def gen():
    i=1
    while True:
        if i>1:
            for j in range(2,i):
                if i % j==0:
                    break
                else:
                    yield i
        i+=1
for t in gen():
    print(t)