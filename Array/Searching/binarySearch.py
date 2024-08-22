# define a binarysearch function
def binarySearch(arr, x, start, end):
    while start <= end:
        mid = start+(end-start)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            return binarySearch(arr, x, mid+1, end)
        else:
            return binarySearch(arr, x, start, mid-1)
    else:
        return -1


# initialzation of array
arr = [10, 20, 30, 40, 50, 60, 70, 80, 90]
x = 10
start = 0
end = len(arr)-1
result = binarySearch(arr, x, start, end)
print("The Element at index is :", result)
