from typing import List
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        i=0
        wealth=[]
        for i in range(len(accounts)):
            a=sum(accounts[i])
            wealth.append(a)
        a=max(wealth)
        return a
            
        

       