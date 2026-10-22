import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l = 1
        r = max(piles)
        min_k = float('inf')

        while l <= r:
            total = 0
            mid = (l + r) // 2
            for pile in piles:
                total = total + math.ceil(pile/mid)
            if total <= h:
                min_k = min(min_k, mid)
                r = mid - 1
            else:
                l = mid + 1
        return min_k