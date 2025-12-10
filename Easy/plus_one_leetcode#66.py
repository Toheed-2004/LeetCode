class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        
        if len(digits)==1:
            if digits[0]!=9:
                digits[0]=digits[0]+1
            else:
                digits[0]=1
                digits.append(0)
            return digits
        else:
            carry=False
            for i in range(-1,-len(digits)-1,-1):
                if digits[i]==9:
                    digits[i]=0
                    carry=True
                else:
                    digits[i]=digits[i]+1
                    return digits
            if carry:
                digits.insert(0,1)
            return digits
                

                

            
        