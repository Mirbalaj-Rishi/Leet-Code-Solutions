
# https://leetcode.com/problems/remove-element/?envType=study-plan-v2&envId=top-interview-150 
nums = [0,1,2,2,3,0,4,2]
val = 2


#submitted code
i = len(nums) - 1
while i != -1:
    if nums[i] == val:
        nums.remove(val)
    i -= 1
    



print(nums)