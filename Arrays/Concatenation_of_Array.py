from typing import List
class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        ans=[]
        i=0
        for i in range(len(nums)):
            ans.append(nums[i])
        
        if len(ans)==len(nums):
            for i in range(len(nums)):
                ans.append(nums[i])
                
        return ans
        