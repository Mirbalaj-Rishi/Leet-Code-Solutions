#https://leetcode.com/problems/two-sum/
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int):
        length = len(nums)
        if length % 2:
            size = length+1
        else:
            size = length
        hash = [[] for i in range(size)]
        #print(hash)
        for index in range(len(nums)):
            compliment = target - nums[index]
            #print(compliment,hash[compliment % size])
            #print(nums.index(compliment))
            if compliment in hash[compliment % size]:
                return [nums.index(compliment), index]
            loc = nums[index]%size
            hash[loc].append(nums[index])

            

        
test = Solution()
print(test.twoSum([3,2,4],6))