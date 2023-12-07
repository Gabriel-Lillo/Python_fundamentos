



class Usuario:

    def __init__(self, username, password):
        self.username = username
        self.password = password


user1 = Usuario()
user2 = Usuario()
user3 = Usuario()

print(user1.__dict__)
print(user2.__dict__)
print(user3.__dict__)