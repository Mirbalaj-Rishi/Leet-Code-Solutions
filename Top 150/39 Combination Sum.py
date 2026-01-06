#https://leetcode.com/problems/combination-sum/
"""
using recursive sub traction to solve 
eg [2,3,4] 7
7 - 3 = 4 
4 - 4 = 0 
combo [3,4]
"""
from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.globalCombos = [] #needed since leetcode does not create a new class
        self.recuriveSubtract(candidates, target)
        return self.globalCombos
    def recuriveSubtract(self, candidates:List[int], target:int, potentialCombo:List[int] = []) -> None: #modifies globalCombos
        candidates.sort()
        for num in candidates:
            tempCombo = potentialCombo.copy() # tempCombo = potentialCombo wont work since it creates a reference
            awnser = target - num
            tempCombo.append(num)
            if awnser >= candidates[0]:
                self.recuriveSubtract(candidates, awnser,tempCombo) #awnser becomes the new target so that we can find a way to finish an unresolved combo
            elif awnser == 0:
                #print(f"combo found {tempCombo}")
                #check if its already in globalCombos
                tempCombo.sort()
                if tempCombo not in self.globalCombos:
                    self.globalCombos.append(tempCombo)
            else:
                #print(f"tempCombo didnt work {tempCombo}")
                pass

test = Solution()
test.combinationSum([2,3,5],8)
print(test.globalCombos)
for i in test.globalCombos:
    print(i)