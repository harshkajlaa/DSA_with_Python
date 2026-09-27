class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length=0
        for i in range(len(s)):
            dict1={}
            for j in range(i,len(s)):
                if s[j] not in dict1:
                    dict1[s[j]]=1
                else:
                    break
            if len(dict1)>max_length:
                max_length=len(dict1)
                
        return max_length