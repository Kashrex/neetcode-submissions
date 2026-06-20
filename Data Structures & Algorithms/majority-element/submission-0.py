class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        n=len(nums)
        dicpi={}
        for x in nums:
            if x in dicpi:
                dicpi[x]+=1
            else:
                dicpi[x]=1
        for key,value in dicpi.items():
            if value>n//2:
                return key
