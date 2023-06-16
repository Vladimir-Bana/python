            #№1
#import random
#n=int(input("Введите количество рядков"))
#m=int(input("Введите количество столбцов"))
#a=[[i]*m for i in range(n)]
#print(a)
#for i in a:
#    print(i)
            #№2
#import random
#n=int(input("Введите количество рядков"))
#m=int(input("Введите количество столбцов"))
#a=[[random.randint(1,9) for j in range(m)] for i in range(n)]
#print(a)
#print("-"*30)
#for i in a:
#    print(f"\n|{i}|")
            #№3
#import random
#n=int(input("Введите количество рядков"))
#m=int(input("Введите количество столбцов"))
#a=[[random.randint(1,9) for j in range(m)] for i in range(n)]
#print(a)
#print("-"*30)
#for i in a:
#    print(f"\t|{i}|")
#c=[a[i][j]for i in range(n) for j in range(m) if i==j]
#print(c)
#e=[a[i]for i in range(m) if i==3]
#print(e)
#v=[a[j]for j in range(n) if j==4]
#print(v)

