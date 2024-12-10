# main.py
from use_cases.blog import CreateBlog
from interfaces.IBlog import CLI
from infrastructures.db import DB

def main():
    db = DB()
    cli = CLI()
    use_case = CreateBlog(db)

    title, content, author = cli.get_input()
    blog = use_case.execute(title, content, author)
    
    cli.display_output(blog)

if __name__ == "__main__":
    
    main()
