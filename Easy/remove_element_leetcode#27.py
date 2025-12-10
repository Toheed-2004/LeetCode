class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
       indexes=[]
       for idx,num in enumerate(nums):
        if num==val:
            indexes.append(idx)
        
       for idx in reversed(indexes):
        nums.pop(idx)

       return len(nums)



