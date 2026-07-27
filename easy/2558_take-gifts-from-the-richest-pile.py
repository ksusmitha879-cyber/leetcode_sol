import heapq,math

from narwhals import List
class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts=[-g for g in gifts]
        heapq.heapify(gifts)
        while k:
            x=-heapq.heappop(gifts)
            heapq.heappush(gifts,-int(math.sqrt(x)))
            k-=1
        return -sum(gifts)