class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        for i in range(len(nums)):
            value = nums[i]
            if value != i:
                return i
        return len(nums)
        
        