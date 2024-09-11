# Optimal code using Binary search
# function defination
def search2DArray(arr, target, left, right):
    while left <= right:
        mid = left+(right-left)//2
        mid_element = arr[mid//n][mid % n]

        if target == mid_element:
            return True
        elif target <= mid_element:
            right = mid-1
        else:
            left = mid+1
    return False


# Brute Force apporach
# def search2DArray(arr, target):

#     for i in range(len(arr)):

#         for j in range(len(arr[i])):

#             if arr[i][j] == target:
#                 return True

#     return False


# driver code
arr = [[1, 3, 5, 7],
       [10, 11, 16, 20],
       [23, 30, 34, 60]]
m = len(arr)
n = len(arr[0])
left = 0
right = m*n-1
target = 7
result = search2DArray(arr, target, left, right)
print(result)
