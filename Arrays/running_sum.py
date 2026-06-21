class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        running_sum=[]
        running_total=0
        n=len(nums)
        for i in range(0,n):
            running_total=running_total+nums[i]
            running_sum.append(running_total)
        return running_sum