class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicti=dict()
        chopa=list()
        for i,x in enumerate(nums):
            compli=target-x
            if compli in dicti:
                chopa.append(dicti[compli])
                chopa.append(i)
                return chopa
            else:
                dicti[x]=i