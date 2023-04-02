'''
    Problem Statement:
        You are given list of numbers, obtained by rotating a sorted list an unknown number of times.
        Write a function to determine the minimum number of times the original sorted list was rotated to obtain the given list.
        Your function should have the worst-case complexity of `O(log N)`, where N is the length of the list. 
        You can assume that all the numbers in the list are unique.
        Example: The list `[5, 6, 9, 0, 2, 3, 4]` was obtained by rotating the sorted list `[0, 2, 3, 4, 5, 6, 9]` 3 times.

        We define "rotating a list" as removing the last element of the list and adding it before the first element. 
        E.g. rotating the list `[1, 2, 3, 4]` produces `[4, 1, 2, 3]`. 

        "Sorted list" refers to a list where the elements are arranged in the increasing order  e.g. `[1, 3, 5, 7]`.


    Solution:
        (BruteForce) Iterate through the array and check which element from the array is greater than the last element. The counted value will be the answer.

    Input: [5, 6, 9, 0, 2, 3, 4]
    Output: 3        

    Here the roations will be equal to the position of the smallest number.
    so we have to check if the number comming after a number is smaller then it or not.
'''

''' Brute Force Solution. (Inefficient)'''
# class Solution:
#     def find_rotation(self, array):
#         for i in range(0, len(array)):
#             if array[i+1] < array[i]:
#                 return i+1
#         return -1
    
# solution = Solution()


''' Efficient '''

class Solution:
    def find_rotation(self, array):
        return self.binary_search(0, len(array)-1, array)

    def binary_search(self, left, right, array):
        while left <= right:
            mid = (left+right)//2
            
            # Vizualisation
            print("mid: ", mid, ", left: ", left, ", right: ", right)
            
            '''len(array)-1 makes sure last elem is not checked cuz m+1 will be invalid.'''
            if mid<len(array)-1 and array[mid] > array[mid+1]:
                return mid+1
            elif array[mid] > array[len(array)-1]:
                left = mid+1
            else:
                right = mid-1
        return -1

solution = Solution()
print(solution.find_rotation([3, 4, 5, 6, 7, 8, 1]))