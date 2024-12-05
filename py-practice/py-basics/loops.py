#  -------- while loop ----------
# li = ["hello", "world", "how", "are", "you"]
# i= 0
# while(i<len(li)):
#     print(li[i])
#     i += 1

# -------- for loop ----------
# for variable in range(n) will print upto n-1 from 0

# for i in range(4):
#     print(i) 

# for i in range ( 1, 5, 2):
#     print(i)

# t= ("hello", "world", "how", "are", "you")
# for i in t:
#     print(i)

# st = "hello"
# for i in st:
#     print(i)

# li = ["hello", "world", "how", "are", "you"]
# for i in range(len(li)):
#     print(li[i], end=" ")
# print("\nAll are printed")

# for i in range(20):
#     if(i == 5):
#         break
#     print(i) break when i = 5 and loop stops

# for i in range (1, 20, 2):
#     if(i == 6):
#         continue
#     print(i, end=" ")


# stud_scores = {
#     "Bidur": 30,
#     "Ajay": 40,
#     "Ankit": 50
# }

# for stud, score in stud_scores.items():
#     print( f"Student name is: {stud} with score: {score}")



# double loop to find key and values 
students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob": {"age": 22, "grade": "B"},
}

for name, details in students.items():
    print("=================================")
    print(name)
    for key, values in details.items():
        print(f" {key} {values}")