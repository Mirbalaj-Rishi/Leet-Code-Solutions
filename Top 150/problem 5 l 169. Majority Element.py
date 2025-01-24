#https://leetcode.com/problems/majority-element/description/?envType=study-plan-v2&envId=top-interview-150


nums = [3,3,4]

#submitted code

countNums = {}
for i in nums: 
    try:
        countNums[i] += 1
    except:
        countNums[i] = 1
    #print(f"i {i} | countNums {countNums}")


maxKey = -1
maxValue = -1
for key, value in countNums.items():
    if value > maxValue:
        maxValue = value
        maxKey = key


print(maxKey) #replace print with return in submission