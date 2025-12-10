class Solution:
    def reverseWords(self, s: str) -> str:
        temp=s.split()
        result=''
        for word in temp:
            result+=word[::-1]+' '
        return result[:-1]



        