# -----1. Follow PEP 8 Guidelines----------------------
# Use 4 spaces per indentation.
# Limit lines to 79 characters.
# Use meaningful variable and function names.
# Add docstrings to modules, classes, and methods using triple quotes.
def greet(name:str):
    """Return a greeting message"""
    return f"Hello, {name}"


# ================2. use list comprehensions-------------------

# ====bad====
# squere = []
# for i in range(12):
#     squere.append(i**2)

# ====good====

squares = [i**2 for i in range(5)]
