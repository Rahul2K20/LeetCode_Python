from typing import List

#Naive
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]

#Optimal
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hmap = {}
        for i in range (len(nums)):
            x = target - nums[i]
            if x not in hmap:
                hmap[nums[i]] = i
            else:    
             return [hmap[x], i]
            
        