class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        flag=True
        answer=""
        lengths=[len(s) for s in strs]
        for i in range (min(lengths)):
            current_char=strs[0][i:i+1]
            for string in strs:
                if string==strs[0]:
                    continue
                if current_char==string[i:i+1]:
                    pass
                else:
                    flag=False
            if flag==False:
                return answer
            else:
                answer+=current_char
        return answer        



