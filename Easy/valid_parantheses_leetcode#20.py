class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        opening_brackets=['(','{','[']
        is_valid=True
        if s.startswith((')',']','}')):
            return False
        for char in s:
            if char in opening_brackets:
                stack.append(char)
            if len(stack)!=0 and char not in opening_brackets:
                top=stack.pop() # top denotes last opening bracket
                if top+char in ["()","[]","{}"]: 
                    continue
                else:
                    is_valid=False
                    return is_valid
            if len(stack)==0 and char in ['}',']',')']: # if last char is a closing bracket ,and there is nothing left to be popped from the stack
                is_valid=False
                return is_valid
        return len(stack)==0
        
        

        







        