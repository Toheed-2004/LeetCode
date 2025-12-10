class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            columnNumber -= 1                      # align A with 0
            remainder = columnNumber % 26
            result += chr(remainder + 65) 
            columnNumber //= 26
        return result[::-1]

        