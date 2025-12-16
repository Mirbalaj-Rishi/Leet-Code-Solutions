#https://leetcode.com/problems/plus-one/description/
from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        startingPlace = len(digits) -1 
        digits = self.addValRecersive(digits, startingPlace)
        return digits
    
    def addValRecersive(self, digits: List[int], place:int, addVal:int = 1) -> List[int]:
        singleDigit = digits[place]
        singleDigit += addVal
        carryOver = 0
        
        if singleDigit > 9:
            carryOver = singleDigit - 9
            singleDigit = 0
        
        digits[place] = singleDigit

        #print(f"singleDigit {singleDigit} carryOver {carryOver} digits {digits} place {place}")
        if carryOver != 0:
            if place != 0:
                place -= 1
            else:# if leading digit needs to change eg 1,9
                place = 0 
                digits.insert(0,0)
            digits = self.addValRecersive(digits, place, carryOver)
        
        return digits
    

test = Solution()
val = test.plusOne([9])
print(val)