class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        result = ""
        for i in range(0, len(s), 2 * k):
            # Get the next 2k chunk (or whatever remains)
            chunk = s[i:i + 2 * k]
            
            if len(chunk) < k:
                # Reverse all characters
                result += chunk[::-1]
            elif len(chunk) < 2 * k:
                # Reverse first k, leave the rest
                result += chunk[:k][::-1] + chunk[k:]
            else:
                # Reverse first k, leave the rest
                result += chunk[:k][::-1] + chunk[k:]
        
        return result



        

        