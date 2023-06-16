# class Rectangle():
#   def __init__(self, st1, st2, s):
#     self.st1 = st1
#     self.st2 = st2
#     self.s = s
#     self.s = self.st1*self.st2
#   def vivod(self):
#     print(f"Площадь: {self.s}")
# a = int(input("Длина: "))
# width = int(input("Ширина: "))
# st1 = Rectangle(a, width, 0)
# st1.vivod()

# class Processing():
#   def __init__(self, input, output):
#     self.input = input
#     self.output = output
#   def b(self, a):
#     print(a.upper())
# a = input("Строка: ")
# c = Processing("","")
# c.b(a)

# class Shop():
#   def __init__(self, name, type):
#     self.name = name
#     self.type = type
#     self.number = 0
#   def open(self):
#     print("Open!")
#   def describe(self):
#     print(f"Name: {self.name}, Type: {self.type}")
#   def Number(self):
#     print(f"Unit: {self.number}")
#   def increment(self, a):
#     self.number += a
# a = int(input("Number="))
# c = Shop("ATB", "products")
# c.increment(a)
# c.Number()
# c.open()
# c.describe()

# class Discount(Shop):
#   def __init__(self, products):
#     self.products = products
#   def get_products(self):
#     print(f"Discount products: {self.products}")
# store = Discount("Ashan, Ashan")
# store.get_products()

class Bank():
  def __init__(self, vnos, zaberat):
    self.bal = 0
    self.vnos = vnos
    self.zaberat = zaberat
  def bal(self):
    print(f"На балике: {self.bal}")
  def deposit(self):
    self.bal += o
  def zaberat_s_banka(self):
    a = int(input("Сколько вы хотите снять: "))
    if self.bal >= a:
      self.bal -= a
    else:
      print("vi bomj")     
print("ДОбро пожаловать в наш банк")
o = int(input("Сколько вы хотите положить: "))
b = Bank(100, 0)
b.deposit()
b.bal()
b.zaberat_s_banka()
b.bal()