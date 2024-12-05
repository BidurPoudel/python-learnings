# name = "bidur poudel"
# print(len(name))
# print(name.startswith("bidur"))
# print(name.endswith("bidur"))

# print(name.replace("poudel", "coder")) replace poudel with coder
# print(name.split(","))
# name2 = ["hello", "world"]
# print(" ".join(name2))
# for i in name:
#     print(i.strip(), end=" ")


class User:
    def __init__(self, username, email,phoneNumber):
        self.username = username
        self.email = email
        self.phoneNumber = phoneNumber

    def __str__(self):
        return f"User's \nname: {self.username}\nemail: {self.email}\nphone number: {self.phoneNumber}"


user = User("john", "john@example.com", "1234567890")
print(user)
# print(user)  # Output: User(johndoe, john@example.com)

username:str= 'Bidur'


