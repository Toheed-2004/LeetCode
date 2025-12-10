class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if s.find(" ")==-1:
            return len(s)
        else:
            list_of_words=s.split()
        answer=list_of_words[-1]
        return len(answer)
            
        