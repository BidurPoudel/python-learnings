def insertion_sort(arr:list[int]):
    
    for i in range(1,len(arr)):
        key = arr[i] 
        j = i - 1
        while j>=0 and arr[j]>key:
            arr[j+1] = arr[j]        
            j -= 1
            arr[j+1] = key
    return arr



sorting = insertion_sort([2,1,3,5,9,4,6])
print(sorting)
