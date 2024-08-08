class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        counter_1 =0
        
        for num in nums:
            remainder = num % 3
            if remainder == 1:
                counter_1 += 1
            elif remainder == 2:
                counter_1 += 1
        
        return counter_1
