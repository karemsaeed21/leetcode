class Solution(object):
    def majorityElement(self, nums):
        return max(set(nums), key=nums.count) 
        