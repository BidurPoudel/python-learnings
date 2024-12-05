
no_dups = set()
duplicates = []

def remove_duplicate(arr):
    for lists in arr:
        if lists not in no_dups:
           no_dups.add(lists)
        else:
            duplicates.append(lists)
    return list(no_dups)

print(remove_duplicate([4 ,7 ,6, 4, 10, 10, 9, 3, 7, 7, 5] ))

