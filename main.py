import random;

def quicksort(arr):
    if (len(arr)<2):
        return arr
    idx = random.randrange(0,len(arr))    
    pivot = arr[idx];
    smaller = []
    larger = []
    for i in range(len(arr)):
        if i!=idx:
            if arr[i]<=pivot:
                smaller.append(arr[i])
            else:
                larger.append(arr[i])

    return quicksort(smaller)+[pivot]+quicksort(larger)

print(quicksort([5,5,4,3,2,2,1]))
