#CODE LINK: https://leetcode.com/problems/single-number/

class Solution(object):
    def singleNumber(self, nums):
        d ={}
        for i in nums:
            if i in d:
                d[i]+=1
            else:
                d[i]=1
        for i in d:
            if d[i] == 1:
                return i
        
        
