class User:
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.login_attempts=0
        self.age=age
    def describe_user(self):
        print(self.first_name,self.last_name)
    def dreeting_user(self):
        print(f"Приветствую, {self.first_name} {self.last_name}!")
    def increment_login_attempts(self):
        self.login_attempts+=1
        print(f"Количество попыток входа в аккаунт: {self.login_attempts}")
    def reset_login_attempts(self):
        self.login_attempts*=0
        print(f"Количество попыток входа в аккаунт: {self.login_attempts}")