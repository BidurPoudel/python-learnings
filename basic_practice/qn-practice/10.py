# finding size of tuple

# -------------------------- finding using sys module -----------------------
# import sys

# tuple_size1 = ("A", 1,2,3)
# tuple_size2 = ("Ram", "Hari", "Vishnu")
# tuple_size3 = ((1, "Bidur"), (2, "Ankit"), (3, "Ajay"), (4, "Milan"))

# print(f"Size of first tuple is: {sys.getsizeof(tuple_size1)}")
# print(f"Size of second tuple is: {sys.getsizeof(tuple_size2)}")
# print(f"Size of third tuple is: {sys.getsizeof(tuple_size3)}")



# -------- using inbuilt __sizeof__ method ----------------
tuple_size1 = ("A", 1,2,3)
tuple_size2 = ("Ram", "Hari", "Vishnu")
tuple_size3 = ((1, "Bidur"), (2, "Ankit"), (3, "Ajay"), (4, "Milan"))

def tuple_size(tuples):
    return str(tuples.__sizeof__())

print(f"size of first tuple is: {tuple_size(tuple_size1)}")
print(f"size of second tuple is: {tuple_size(tuple_size2)}")
print(f"size of third tuple is: {tuple_size(tuple_size3)}")