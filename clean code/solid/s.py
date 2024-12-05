class Book:
    def __init__(self, title:str, author:str):
        self.title = title
        self.author= author
    
    def book_details(self):
        return f"title is{self.title}\nage is{self.author}"


class Notify:
    pass