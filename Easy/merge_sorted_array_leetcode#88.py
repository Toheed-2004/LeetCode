class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:] = sorted(nums1[:m] + nums2)


        # if len(nums2)==0:
        #     return nums1
           
        # nums1=nums1[:m]
        # nums1.extend(nums2)
        # nums1.sort()
        # for i in range(len(nums1)):
        #     nums1[i]=nums1[i]
        