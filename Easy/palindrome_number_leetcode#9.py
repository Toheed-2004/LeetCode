class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x=str(x)
        start_idx=0
        end_idx=len(x)-1
        is_palindrome=True
        for i in range(int(math.ceil(len(x)/2))):
            if x[start_idx]==x[end_idx]:
                start_idx+=1
                end_idx-=1

            else:
                is_palindrome=False
                return is_palindrome
        return is_palindrome


        