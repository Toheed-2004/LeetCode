class Solution:
    def firstUniqChar(self, s: str) -> int:
        s=list(s)
        count=Counter(s)
        for char in s:
            if count[char]>1:
                continue
            else:
                return s.index(char)
        return -1