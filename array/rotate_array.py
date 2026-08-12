def rotateLeft(arr, d):
    n = len(arr)
    if n == 0:
        return
    
    d = d % n  # handle d > n (circular)
    
    # Step 1: Reverse first d elements
    reverse(arr, 0, d - 1)
    # Step 2: Reverse the remaining n-d elements
    reverse(arr, d, n - 1)
    # Step 3: Reverse the entire array
    reverse(arr, 0, n - 1)

def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

