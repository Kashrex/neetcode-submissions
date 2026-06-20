# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         if not nums1:
#             return nums2
#         if not nums2:
#             return nums1
#             p,q=0,0
#         if m>n:
#             tomo=[]
#             for x in range(m):
#                 nums1[p]>nums2[q]:
#                 tomo[x]=nums[q]
#                 q+=1
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = m - 1          # pointer for nums1 valid elements
        j = n - 1          # pointer for nums2
        k = m + n - 1      # write pointer (end of nums1)

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1