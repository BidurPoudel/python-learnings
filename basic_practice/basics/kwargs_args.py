# def greet_peopele(*args):
#     print(args)
#     for name in args:
#         print(f"hello {name} welcome to python practice course")


# greet_peopele("bidur", "ajay", "ankit", "milan")

def greet_multi_people(**kwargs):
    print(kwargs)
    for name, age in kwargs.items():
        print(f"{name}, your age is {age}")


greet_multi_people(bidur=24, ajay=25, ankit=26)