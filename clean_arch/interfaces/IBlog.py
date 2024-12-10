# interfaces/cli.py
class CLI:
    def get_input(self):
        title = input("Enter blog title: ")
        content = input("Enter blog content: ")
        author = input("Enter author name: ")
        return title, content, author

    def display_output(self, blog):
        print("\nBlog Created Successfully!")
        print(f"Title: {blog.title}")
        print(f"Content: {blog.content}")
        print(f"Author: {blog.author}")
