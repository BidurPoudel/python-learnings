#  in use cases we encapsulate the business logic 
# for now Manages creating a blog while ensuring business rules are followed.

from entities.blog_entity import Blog
from infrastructures.db import DB

class CreateBlog:
    def __init__(self, db:DB):
        self.db = db

    def execute(self, title:str, author: str, content: str):
        if not title and content:
            raise ValueError("Title or content is missing")
        blog = Blog(title, content, author)
        self.db.save(blog)
        return blog
        
        