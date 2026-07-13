class Solution:
    def reversePairs(self, nums: List[int]) -> int: # type: ignore
        if not nums:
            return 0
        return self.merge_sort(nums, 0, len(nums) - 1)

    def merge_sort(self, nums, left, right):
        if left >= right:
            return 0
        
        mid = (left + right) // 2
        count = self.merge_sort(nums, left, mid) + self.merge_sort(nums, mid + 1, right)
        
        j = mid + 1
        for i in range(left, mid + 1):
            while j <= right and nums[i] > 2 * nums[j]:
                j += 1
            count += (j - (mid + 1))
        
    
        nums[left:right + 1] = sorted(nums[left:right + 1])
        return count