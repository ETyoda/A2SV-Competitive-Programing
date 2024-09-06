from collections import defaultdict

class Solution:
    def firstUniqChar(self, s: str) -> int:
        freqOfChar = defaultdict(int)
        for char in s:
            freqOfChar[char] += 1
        for index in range(len(s)):
            char = s[index]
            if freqOfChar[char] == 1:
                return index
        return -1