#https://leetcode.com/problems/merge-sorted-array/submissions/1511121694/?envType=study-plan-v2&envId=top-interview-150

#couldn't use the = operator since it creates a new list that replaces the orignial nums1 do I needed to do something else
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3

#Submitted Code
m -= 1
twoLoc = n - 1

for i in range(m+1,m+n+1):
    nums1[i] = nums2[twoLoc]
    twoLoc = twoLoc - 1

nums1.sort()

print(nums1)