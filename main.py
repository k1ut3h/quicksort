def quicksort(arr):
    if (len(arr)<2):
        return arr
    if (len(arr)==2):
        if (arr[1]<arr[0]):
            arr[0], arr[1] = arr[1], arr[0]
        return arr
    pivot = arr[0];
    smaller = [i for i in arr[1:] if i<=pivot]
    larger = [i for i in arr[1:] if i>pivot]

    return quicksort(smaller)+[pivot]+quicksort(larger)

print(quicksort([10,10,5,1,3,546,2342,5,3,23,52,2]))
