class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        hashMap = {}
        for string in strs:
            newString = "".join(sorted(string))
            if newString in hashMap:
                hashMap[newString].append(string)
            else:
                hashMap[newString] = [string]
        output = list(hashMap.values())
        return output