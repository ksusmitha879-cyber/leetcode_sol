class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n=len(nums)
        ans=[]
        nums.sort()
        for i in range(n-3):
            if i>0 and nums[i] == nums[i-1]:
                continue
            if nums[i]+nums[i+1]+nums[i+2]+nums[i+3]>target:break
            if nums[i]+nums[n-3]+nums[n-2]+nums[n-1]<target:continue
            for j in range(i+1,n-2):
                if j>i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i]+nums[j]+nums[j+1]+nums[j+2]>target:break
                if nums[i]+nums[j]+nums[n-2]+nums[n-1]<target:continue
                l,h=j+1,n-1
                while l<h:
                    s=nums[i]+nums[j]+nums[l]+nums[h]
                    if s==target:
                        ans.append([nums[i],nums[j],nums[l],nums[h]])
                        l+=1
                        h-=1
                        while l<h and nums[l]==nums[l-1]:l+=1
                        while l<h and nums[h]==nums[h+1]:h-=1
                    elif s<target:
                        l+=1
                    else:
                        h-=1
        return ans
