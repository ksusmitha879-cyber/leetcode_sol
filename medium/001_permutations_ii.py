class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]: # type: ignore
        res = []
        def solve(index):
            if index == len(nums):
                res.append(nums[:])
                return
            used = set()
            for i in range(index,len(nums)):
                if nums[i] in used:
                    continue
                used.add(nums[i])
                nums[index],nums[i] = nums[i],nums[index]
                solve(index+1)
                nums[index],nums[i] = nums[i],nums[index]
        solve(0)
        return res           