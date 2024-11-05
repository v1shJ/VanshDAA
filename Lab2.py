def linear(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

def binary(arr, target, left = 0, right = None):
    if right == None:
        right = len(arr)-1
    middle = (left+right)//2
    if left > right:
        return -1
    elif arr[middle] == target:
        return middle
    elif arr[middle] > target:
        return binary(arr, target, left, middle-1)
    else:
        return binary(arr, target, middle+1, right)
    
    

print(linear([1, 2, 3, 7, 9], 135))
print(linear([], 135))
print(linear([15, 16, 17, 19], 16))
print(linear([1, 2, 3, 4, 5], 1))
print(linear([97, 98, 99, 100], 100))

print("\n\n")

print(binary([1, 2, 3, 7, 9], 5))
print(binary([], 5))
print(binary([135, 32, 29, 70, 6], 29))
print(binary([0, 1, 2, 3, 4], 0))
print(binary([0, 1, 2, 3, 4], 4))
