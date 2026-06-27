# class Solution:
#     def gethours(self, piles):

#     def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         l=1
#         r=max(piles)
#         ans = r
#         while l<=r:
#             mid = l+ (r-l)//2
#             hour = 0
#             for pile in piles:
#                 hour=ciel(pile/mid)

from typing import List

class Solution:
    def getHours(self, piles: List[int], speed: int) -> int:
        total_hours = 0

        for pile in piles:
            hours = pile // speed
            if pile % speed != 0:
                hours += 1
            total_hours += hours

        return total_hours

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r

        while l <= r:
            mid = (l + r) // 2

            if self.getHours(piles, mid) <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1

        return ans