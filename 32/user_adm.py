from User  import *
from Admin import *
 
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