def merge_list(list1, list2):
    empty_list = []
    for j in range(len(list2)):
        print(list1[j])
        if (list1[j] % 2 != 0):
            empty_list.append(list1[j])
            print(empty_list)
    for i in range(len(list2)):
        if (list2[i] % 2 == 0):
            empty_list.append(list2[i])
    return empty_list
list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]
print("result is: ", merge_list(list1, list2) )

