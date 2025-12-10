class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s,t=str(sorted(s)),str(sorted(t))
        if s==t:
            return True
        else:
            return False
        