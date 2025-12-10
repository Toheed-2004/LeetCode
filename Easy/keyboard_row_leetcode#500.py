class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        result=[]
        rows=['dummy','qwertyuiop','asdfghjkl','zxcvbnm']
        for word in words:
            w=word.lower()
            if sorted(set(w+rows[1]))==sorted(rows[1]):
                result.append(word)
            elif sorted(set(w+rows[2]))==sorted(rows[2]):
                result.append(word)
            elif sorted(set(w+rows[3]))==sorted(rows[3]):
                result.append(word)
            else:
                pass
        return result
            
            
            




        