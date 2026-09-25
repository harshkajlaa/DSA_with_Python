class Solution:
    def sortArrayByParity(self, nums: list[int]) -> list[int]:
        if len(nums)==0:
            return nums 
        start=0
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                nums[start],nums[i]=nums[i],nums[start]
                start+=1
                
        return nums 