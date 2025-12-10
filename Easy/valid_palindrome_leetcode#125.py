class Solution:
    def isPalindrome(self, s: str) -> bool:
        alpha_numeric_characters=r'[a-zA-Z0-9]'
        s=re.findall(alpha_numeric_characters,s)
        s = ''.join(map(str, s))
        s=s.lower()
        if s==s[::-1]:
            return True
        else:
            return False



        