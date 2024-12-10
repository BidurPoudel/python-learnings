class DB:
    def __init__(self) -> None:
        self.storage = []
    
    def save(self, blog):
        self.storage.append(blog)
    
    def list_blogs(self):
        return self.storage
    