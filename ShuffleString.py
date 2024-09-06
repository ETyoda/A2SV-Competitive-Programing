class Solution:
    def restoreString(self, s: str, indices: list[int]) -> str:
        shuffled = [''] * len(s)
        for i, char in enumerate(s):
            shuffled[indices[i]] = char
        return ''.join(shuffled)