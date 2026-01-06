#https://leetcode.com/problems/two-sum/
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        for index1 in range(len(nums)):
            for index2 in range(len(nums)):
                if index2 == index1:
                    continue
                elif nums[index1] + nums[index2] == target:
                    return [index1, index2]
        
test = Solution()
print(test.twoSum([3,2,4],6))