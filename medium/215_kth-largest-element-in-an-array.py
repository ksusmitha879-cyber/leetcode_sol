class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int: # type: ignore
        minheap=[]
        for num in nums:
            if len(minheap)<k:
                heapq.heappush(minheap,num) # type: ignore
            else:
                if num>minheap[0]:
                    heapq.heappop(minheap) # type: ignore
                    heapq.heappush(minheap,num) # type: ignore
        
        return minheap[0]