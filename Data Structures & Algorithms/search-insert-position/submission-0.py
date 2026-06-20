class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        res=len(nums)
        high = len(nums)-1
        while low<=high:
            mid= low+(high-low)//2
            if nums[mid]==target:
                return mid
            elif nums[mid]<target:
                low=mid+1
            else:
                res=mid
                high=mid-1
        return res