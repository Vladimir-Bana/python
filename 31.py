class User:
    def __init__(self,first_name,last_name,age,citi,login_attempts):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
        self.citi=citi
        self.login_attempts=login_attempts
    def describe_user(self):
        print(f"Your name = {self.last_name} {self.first_name}")
    def greeting_user(self):
        print(f"hi{self.last_name} {self.first_name} , your age={self.age}, your citi={self.citi}")
    def increment_login_attempts(self):
        
p=User("Vova","Nedb",15,"UA")
p.describe_user()
p.greeting_user()