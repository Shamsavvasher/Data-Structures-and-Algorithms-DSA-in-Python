# define a function of linearSearch
def linearSearch(arr, x):
    for i in range(0, len(arr)-1):
        if arr[i] == x:
            return i
    else:
        return -1


# initalization of array
arr = [10, 20, 30, 40, 50, 60]
x = 50

result = linearSearch(arr, x)
print(result)
