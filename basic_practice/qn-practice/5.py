def check_number(numberList):
    print(f"Given list is: {numberList}")
    firstNumber = numberList[0]
    lastNumber = numberList[-1]
    if (firstNumber == lastNumber):
        return True
    else:
        return False
    

numbers_x = [10, 20, 30, 40, 10]

print("result is: ", check_number(numbers_x))