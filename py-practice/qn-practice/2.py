print("Printing current and previous number sum in a range(10)")
prev_num = 0
for i in range(1, 11):
    sum_number = prev_num + i
    print("Current Number", i, "Previous Number ", prev_num, " Sum: ", sum_number)
    prev_num = i
    
    