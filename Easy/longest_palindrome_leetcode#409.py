class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count=Counter(s)
        middle=False
        result=0
        if len(set(s))==1:
            return len(s)
        for char in char_count:
            if char_count[char]==1 and not middle:
                result+=1
                middle=True
            elif char_count[char]%2==0:
                result+=char_count[char]
            else:
                result+=char_count[char]-1
                if not middle:
                    result+=1
                    middle=True

        return result

        


        