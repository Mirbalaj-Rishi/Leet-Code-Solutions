# https://leetcode.com/problems/search-insert-position/description/

"""
Used binary search to find a number if its in the list 
and to find the index if the number was in the list

implimented binary search without looking at a resource so the code is janky
"""

from typing import List
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = self.binarySearch(nums, target)
        return index

    def binarySearch(self, nums: List[int], target: int, far_left:bool=False) -> int:
        #print("\n-------------------------------")
        

        
        length = len(nums)
        if length == 3:
            left = nums[0]
            middle = nums[1]
            right = nums[2]
            #print(f"left {left} target {target} right {right} nums {nums}")
            if left < target and target < middle:
                return 1
            elif middle < target and target < right:
                return 2
            elif target == left:
                return 0
            elif target == right:
                return 2
            
        if length == 2:
            left = nums[0]
            right = nums[1]
            #print(f"left {left} target {target} right {right} nums {nums}")
            if left < target and target < right:
                return 1
            elif target <= left:
                return 0
            elif target > right:
                return 2
            elif target == right:
                return 1
        
        if length == 1:
            val = nums[0]
            if target > val:
                return 1
            elif target <= val:
                return 0
        
        middle_index = int(length/2)
        middle_num = nums[middle_index]
        
        print(f"mid index {middle_index} mid num {middle_num} length {length} nums {nums}")
        #input()
        if middle_num == target:
            # print("middle")
            return middle_index 
        elif middle_num < target:
            
            
            new_nums = nums[middle_index:]
            #print(f"right {new_nums}")
            index = self.binarySearch(new_nums,target)
            index += middle_index 
            return index
        elif middle_num > target:
            
            new_nums = nums[:middle_index]
            #print(f"left {new_nums}")
            index = self.binarySearch(new_nums,target,True)
            return index    
        return -1
    
    
test = Solution()
print(test.searchInsert([1],0))