# we are finding the second large element among the array

class Solution:
    def getSecondLargest(self, arr):
        first = -1
        second = -1
        
        for num in arr:
            if num > first:
                second = first
                first = num
            elif num > second and num != first:
                second = num
                
        return second

