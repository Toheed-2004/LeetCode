class Solution:
    def reverseVowels(self, s: str) -> str:
        s=list(s)
        vowels=['A','E','I','O','U','a','e','i','o','u']
        vowels_indexes=[idx for idx,char in enumerate(s) if char  in vowels]
        i,j=0,len(vowels_indexes)-1
        while i<j:
            s[vowels_indexes[i]], s[vowels_indexes[j]] = s[vowels_indexes[j]], s[vowels_indexes[i]]
            i += 1
            j -= 1    
        return "".join(s)
                