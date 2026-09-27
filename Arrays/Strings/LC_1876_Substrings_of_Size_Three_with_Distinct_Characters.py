class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count=0
        for i in range(len(s)-2):
            dict1={}
            for j in range(i,i+3):
                if s[j] not in dict1:
                    dict1[s[j]]=1
                else:
                    dict1[s[j]]+=1
            if len(dict1)==3:
                count+=1
        return count