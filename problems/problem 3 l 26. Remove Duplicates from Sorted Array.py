# https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
nums = [0,0,1,1,1,2,2,3,3,4]

# submitted code
listOfDups = []
i = len(nums) - 1
while i != -1:
    value = nums[i]
    if value not in listOfDups:
        listOfDups.append(value)
    else:
        nums.pop(i)
    i -= 1

print(nums)