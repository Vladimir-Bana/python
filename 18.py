                #№1
# spisok_1=[1,2,3]
# spisok_2=[4,6,7]
# spisok=[(a,x) for a in spisok_2 for x in spisok_1 ]
# print(spisok)
                #№2
# slovar={"Item1":1,"Item2":2,"Item3":3,"Item4":4,"Item5":5,"Item6":6}
# slovar2={a:b**2 if b>4 else "false" for a,b in slovar.items() }
# print(slovar2)                
                #№3
# n= int(input("vvesti n:"))
# m= int(input("vvesti m:"))
# massive=[ [0]*n for a in range(m)]
# for b in massive:
#     print(b)                
                #№4
# import random
# n= int(input("vvesti n:"))
# m= int(input("vvesti m:"))
# massive=[ [random.randint(1,9) for r in range(m)] for a in range(n)]
# print("matrica --->")
# for r in massive:
#     print(f"\t\t{r}")
# massive2=[massive[a][r] for a in range(n) for r in range(m) if a==r]
# print(f"Главная диагональ ------> {massive2}")
# massive3=[massive[a][r] for a in range(n) for r in range(m) if a==1]
# print(f"Вторая строка ------> {massive3}")
# massive4=[massive[a][r] for a in range(n) for r in range(m) if r==2]
# print(f"Третий столбец ------> {massive4}")                