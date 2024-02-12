# users = {
#     1: {"name": "name-1", "email": "email1"},
#     2: {"name": "name-2", "email": ""},
#     3: {"name": "name-3", "email": None},
#     4: {"name": "name-4", },
# }
# for user in users.values():  # type: dict
#     if not user.get("email"):
#         print(user.get("name"))

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.password = password
        self.email = email
        self.is_active = False

    def __str__(self):
        return f"name= {self.name}, email= {self.email}"

    def set_name(self, new_name: str):
        self.name = new_name

    def __bool__(self):
        return self.is_active


user1 = User(name="Alex", password="123", email="e-mail")
user2 = User(name="Masha", password="456", email="mylo")
print(user1.password)
print(user2.password)
print(user1)
print(user2.set_name("Maruzhenko"))
print(user2)
