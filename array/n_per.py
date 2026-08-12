class Solution:
    def nextPermutation(self, arr):
        n = len(arr)
        if n <= 1:
            return
        
        # Step 1: Find the pivot (first element from right that is smaller than its next)
        i = n - 2
        while i >= 0 and arr[i] >= arr[i + 1]:
            i -= 1
        
        # Step 2: If pivot exists, find the rightmost successor and swap
        if i >= 0:
            j = n - 1
            while j >= 0 and arr[j] <= arr[i]:
                j -= 1
            arr[i], arr[j] = arr[j], arr[i]
        
        # Step 3: Reverse the suffix starting at i+1
        # (If no pivot was found, i = -1, so we reverse the entire array)
        self.reverse(arr, i + 1, n - 1)
    
    def reverse(self, arr, start, end):
        while start < end:
            arr[start], arr[end] = arr[end], arr[start]
            start += 1
            end -= 1
