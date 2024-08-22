# Two pointer Apporach
# define a function

def twoPointer(arr, sum_value, left, right):
    while left <= right:
        if arr[left]+arr[right] == sum_value:
            return (left, right)
        elif arr[left]+arr[right] > sum_value:
            right -= 1
        else:
            arr[left]+arr[right] < sum_value
            left += 1
    else:
        return -1, -1


# initailzation of array
arr = [20, 40, 60, 80, 90, 120, 240]
sum_value = 210
left = 0
right = len(arr)-1
result = twoPointer(arr, sum_value, left, right)
print(result)
