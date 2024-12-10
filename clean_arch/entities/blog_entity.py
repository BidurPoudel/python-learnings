# in entity-we write core business objects and rules

class Blog:
    def __init__(self, title:str, author:str, content:str) -> None:
        self.title = title
        self.author = author
        self.content = content
        