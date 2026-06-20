class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dicti=dict()
        for x in nums:
            if x in dicti:
                return True
            else:
                dicti[x]=1
        return False