'''
    Problem Statement:
        Given an array of integers in increasing order find the first
        and last position of target element.
        (target elements may be repeating...)
    
    Solution:
        - Perform binary search and for first and last position 
            if the target matches check the left and right elements.

    Input: nums = [5,7,7,8,8,10], target = 8
    Output: [3,4]

    expects -1 for not found..
'''

def binary_search(left, right, position):
    while left <= right:
        mid = (left + right) // 2
        result = position(mid)
        if result == 'found':
            return mid
        elif result == 'right':
            left = mid+1
        else:
            right = mid-1
    return -1

def first_last_position(array, target):
    def left_position(mid):
        if array[mid] == target:
            ''' This checks left element. '''
            if mid-1 >= 0 and array[mid-1] == target:
                return 'left'
            return 'found'
        elif array[mid] > target:
            return 'left'
        else:
            return 'right'
    
    def right_position(mid):
        if array[mid] == target:
            ''' This checks right element '''
            if mid > 0 and array[mid+1] == target:
                return 'right'
            return 'found'
        elif array[mid] > target:
            return 'left'
        else:
            return 'right'
        
    return binary_search(0, len(array)-1, left_position), binary_search(0, len(array)-1, right_position)


''' Obejct Oriented (class Solution) is mandatory name. '''

class Solution:
    def searchRange(self, array, target):
        def left_position(mid):
            if array[mid] == target:
                ''' This checks left element. '''
                # make sure the index of array is valid so mid > 0 is checked in left.
                if mid > 0 and array[mid-1] == target:
                    return 'left'
                return 'found'
            elif array[mid] > target:
                return 'left'
            else:
                return 'right'
        
        def right_position(mid):
            if array[mid] == target:
                ''' This checks right element '''
                # for right index <= last position is valid.
                if mid < len(array)-1 and array[mid+1] == target:
                    return 'right'
                return 'found'
            elif array[mid] > target:
                return 'left'
            else:
                return 'right'
            
        return [self.binary_search(0, len(array)-1, left_position), self.binary_search(0, len(array)-1, right_position)]
    
    def binary_search(self, left, right, position):
        while left <= right:
            mid = (left + right) // 2
            result = position(mid)
            if result == 'found':
                return mid
            elif result == 'right':
                left = mid+1
            else:
                right = mid-1
        return -1

solution = Solution()

tests = [
    {
        "input": {
            "array": [5,7,7,8,8,10],
            "target": 8
        },
        "output": [3,4]
    },
    {
        "input": {
            "array": [5,7,7,8,8,10],
            "target": 6
        },
        "output": [-1,-1]
    },
    {
        "input": {
            "array": [],
            "target": 8
        },
        "output": [-1,4]
    }
    # TODO: Add More...
]

for index, case in enumerate(tests):
    output = solution.searchRange(**case['input'])
    if output == case['output']:
        print(f'Test {index}: Passed')
    else:
        print(f'Test {index}: Failed')
        print('output: ', output)
        print('expected: ', case['output'])
    print('\n')