from typing import List

#Naive
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range (0,len(nums)):
            for j in range (i+1, len(nums)):
                if(nums[i] == nums[j]):
                    return True 
            
        return False 
    
#Optimal approach 1 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hmap = {}
        for i in nums: 
            if i in hmap:
                return True 
            hmap[i] = 1 
        return False 
    
#Optimal approach 2 
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for i in nums:
            if i in seen:
                return True 
            seen.add(i)
        return False 


