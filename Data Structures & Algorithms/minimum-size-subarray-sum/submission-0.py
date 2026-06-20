class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l=0
        n=len(nums)
        sum=0
        mini=float('inf')
        for r in range(n):
            sum+=nums[r]
            while sum >= target:
                mini=min(mini,r-l+1)
                sum-=nums[l]
                l+=1
        if mini == float('inf'):
            return 0
        else:
            return mini