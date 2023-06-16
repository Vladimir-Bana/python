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
class Admin(User):
    def __init__(self,first_name,last_name,age):
        User.__init__(self,first_name,last_name,age)
        self.privileges=["Allowed to delete users","Allowed to add message", "Allowed to ban users"]
    def dreeting_admin(self):
        print(f"Приветствую администрацию, {self.first_name} {self.last_name}!")    
    def show_privileges(self):
        print("Привилегии админа:")
        for i in self.privileges:
            print(i)
class Privileges(Admin):
    def __init__(self,first_name,last_name,age):
        super().__init__(first_name,last_name,age)
        self.privileges=["Allowed to delete users","Allowed to add message", "Allowed to ban users"]
    

user1=User("Недбаевский","Владимир",15)
user1.dreeting_user()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.increment_login_attempts()
user1.reset_login_attempts()
admin1=Admin("Дмитриев","Денис",24)
admin1.dreeting_admin()
priv=Privileges("Дмитриев","Денис",24)
priv.show_privileges()