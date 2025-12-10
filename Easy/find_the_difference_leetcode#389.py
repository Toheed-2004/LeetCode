from collections import Counter
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
            t_count=Counter(t)
            s_count=Counter(s)
            for char in t:
                if char not in s_count:
                    return char
                elif s_count[char]<t_count[char]:
                    return char
                else:
                    pass