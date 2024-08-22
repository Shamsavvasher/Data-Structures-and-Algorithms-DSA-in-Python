# function definition
# Time complexity O(n^2)
def selectionSort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[min_idx] > arr[j]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr

    # driver code
arr = [7, 1, 4, 2, 3]
result = selectionSort(arr)
print("Sorted Elements are using Selection sort:", result)
