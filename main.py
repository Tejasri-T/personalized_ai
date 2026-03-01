def user(name, age):
    class User:
        def __init__(self, name, age):
            self.name = name
            self.age = age
        def __str__(self):
            return f"Name: {self.name}, Age: {self.age}"
    return User(name, age)
if __name__ == "__main__":
    user1 = user("Teja",19)
    print(user1)