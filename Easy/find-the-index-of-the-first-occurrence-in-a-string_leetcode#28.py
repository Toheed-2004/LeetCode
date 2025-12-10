class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(haystack)<len(needle):
            return -1
        elif needle in haystack:
            start=0
            while True:
                if len(haystack[start:])<len(needle):
                    break

                if needle==haystack[start:start+len(needle)]:
                    return start
                start=start+1




        else:
            return -1

        