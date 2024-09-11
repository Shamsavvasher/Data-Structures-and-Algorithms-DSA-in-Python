# define bubble sort function
def BubbleSort(arr):
    n = len(arr)
    for i in range(n):
        # print("\ni-", i, arr)
        for j in range(0, n-i-1):
            # print("\nj-", j, arr)

            if arr[j] > arr[j+1]:
                # arr[j], arr[j+1] = arr[j+1], arr[j] we can solve use this method
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr


# driver code
arr = [59, 20, 5, 43]
result = BubbleSort(arr)
print("Sorted Elements are using Bubble sort:", result)
