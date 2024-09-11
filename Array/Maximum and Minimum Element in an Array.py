#Given an array of size of N. The task is to find the maximum and the minimum
#element of the array using the minimum number of comparisons

def SetMini(arr):
    mini=float('inf')
    for num in arr:
        if num <mini:
            mini=num
    return mini
def SetMaxi(arr):
    maxi=float('-inf')
    for num in arr:
        if num > maxi:
            maxi=num
    return maxi
arr=[1,2,4,5,6]
n=len(arr)
print("Minimum element is :",SetMini(arr))
print("Maximum element is :",SetMaxi(arr))
