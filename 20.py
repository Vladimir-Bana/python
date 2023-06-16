    #1
# def y(n):
#     print("perebor1")
#     yield n
#     print("perebor2")
#     yield n+1
# m=int(input("vvedite --> "))
# v=y(m)
# print(next(v))
# print(next(v))
    #2
# list1=[4,9,16,25,36]
# list2=(i**(0.5) for i in list1)
# print(next(list2))
# print(next(list2))
# print(next(list2))
# print(next(list2))
# print(next(list2))
# print(next(list2))
    #3
list1=["zheka","den","vova","sasha"]
def name():
    for t in list1:
        yield t
a=name()
for i in a:
    print(i)