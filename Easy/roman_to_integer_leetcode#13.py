class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        count=0
        result=0
        roman_to_integer={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        exceptional_cases={'IV':4,'IX':9,'XL':40, 'XC':90, 'CD':400,'CM':900}
        
        while True:
            if count>len(s)-1:
                return result
            
            if not count+1 > len(s)-1:    
                if str(s[count]+s[count+1]) in exceptional_cases:
                    temp=s[count]+s[count+1]
                    result+=exceptional_cases[temp]
                    count+=2
                else:
                    result+=roman_to_integer[s[count]]
                    count+=1
            else:
                    result+=roman_to_integer[s[count]]
                    count+=1