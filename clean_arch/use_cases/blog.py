#  in use cases we encapsulate the business logic 
# for now Manages creating a blog while ensuring business rules are followed.

from entities.blog_entity import Blog

class CreateBlog:
    def __init__(self, db):
        self.db = db

    def execute(self, title:str, author: str, content: str):
        blog = Blog(title, content, author)
        self.db.save(blog)
        return blog
        
        