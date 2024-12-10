# in entity-we write core business objects and rules

class Blog:
    def __init__(self, title:str, author:str, content:str) -> None:
        if not title and content:
            raise ValueError("Title or content is missing")
        self.title = title
        self.author = author
        self.content = content
        