#oops
int1 = 10
print(type(int1))

#opps means binding attributes + methods
class login:
    def __init__(self, username, password):#init is the dender method it works as a constructor, self is a parameter,not a keyword
        self.username = username
        self.password = password

    def display(self):
        print(f"Username: {self.username}, Password: {self.password}")

#create a registration calss with attributes name, email, password and method
class registration:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

    def display(self):
        print(self.name, self.email, self.password)
#object creation
user1 = registration("user123","shabadvignesh@gmail.com", "pass123")
user1.display()

#Virtual environment
#Project food delivery -> python 3.10
#Project music streaming -> python 3.12


#pip install virtualenv
#virtualenv env -> create a virtual environment named env
#source env/bin/activate -> to activate the virtual environment
#pip install flask
#pip freeze -> to see the installed packages
#pip freeze > requirements.txt -> to save the installed packages in a file
#pip install -r requirements.txt -> to install packages from the requirements file