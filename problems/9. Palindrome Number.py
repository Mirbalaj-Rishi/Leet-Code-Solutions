class Solution:
    def isPalindrome(self, x: int) -> bool:
        numString = str(x)
        # if numString[0] == "-":
        #     numString = numString[1:]
        if numString == self.reverseString(numString):
            return(True)
        else:
            return(False)
    def reverseString(self, string_input) -> str:
        new_string:str = ""
       
        for i in range(len(string_input)-1, -1, -1):
            new_string += string_input[i]
        return new_string

s = Solution().isPalindrome(-121)