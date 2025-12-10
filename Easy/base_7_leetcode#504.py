class Solution:
    def convertToBase7(self, num: int) -> str:
        if num==0:
            return '0'
        result=''
        temp=num*-1 if num<0 else num
        while temp>0:
            result=str(temp%7)+result
            temp=temp//7
        
        return result if num>0 else '-'+result
            
        