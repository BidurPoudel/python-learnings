class User:
    def __init__(self, name:str, age:int, address:str) -> None:
        self.name = name
        self.age = age
        self.address = address
    
    def user_details(self):
        print(f"user details:\nname: {self.name}\age: {self.age}\address: {self.address}")


user = User("Bidur", 23, 'Nepal')
user.user_details()

class MailSender:
    def __init__(self, email: str, time: int) -> None:
        self.email = email
        self.time = time
        
    def send_email(self):
        print(f'seding email to: {self.email}')
    
    def send_hotmail(self):
        print(f"{self.email} from hotmail")
emails= MailSender('bidur@gmail.com', 12)
