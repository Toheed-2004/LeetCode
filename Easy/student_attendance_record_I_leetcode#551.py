class Solution:
    def checkRecord(self, s: str) -> bool:

        char_count_dict=Counter(s)
        if char_count_dict['A']<2 and  'LLL' not in s:
            return True
        else:
            return False
            