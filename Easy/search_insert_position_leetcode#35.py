class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target>max(nums):
            return len(nums)
        elif target<min(nums):
            return 0
        elif target in nums:
            return nums.index(target)
        else:
            left,right=0,len(nums)
            while left<right:
                mid=(left+right)//2
                if nums[mid]>target:
                    right=mid
                else:
                    left=mid+1
            return left
                      




        