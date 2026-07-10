class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        if 0 not in nums:
            return 0
        elif len(nums) not in nums: 
            return len(nums)
        else:     
            nums.sort()
            for x in range(len(nums) - 1):
                if nums[x] + 1 != nums[x + 1]:
                    return nums[x] + 1