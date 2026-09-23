# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/?envType=study-plan-v2&envId=top-interview-150
nums = [1,1,1,2,2,3]

# submitted code
listOfDups = []
i = len(nums) - 1
count = 0
previousValue = ""
while i != -1:
    value = nums[i]
    # check to see how many repeats 
    if value == previousValue:
        count += 1
    else:
        count = 0

    # check to see if there are less than 2 repeats 
    if value not in listOfDups or count < 2:
        listOfDups.append(value)
    else:
        nums.pop(i)

    #update previous value
    previousValue = value 
    i -= 1


print(nums)