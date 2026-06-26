class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum=res=nums[0]
        for n in nums[1:]:
            sum=max(n,sum+n)
            res=max(sum,res)
        return res