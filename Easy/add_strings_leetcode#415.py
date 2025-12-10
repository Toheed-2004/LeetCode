class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
            i = len(num1) - 1  # pointer to the last element of num1
            j = len(num2) - 1  # pointer to the last of num2
            carry = 0
            result = []

            while i >= 0 or j >= 0 or carry:#continue untill both lists are not exhausted and carry exists
                x = int(num1[i]) if i >= 0 else 0
                y = int(num2[j]) if j >= 0 else 0

                total = x + y + carry
                carry = total // 10
                result.append(str(total % 10))

                i -= 1
                j -= 1
            return ''.join(result[::-1])
                
            


