class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        x = []
        y = []
        for i in range(n):
            x.append(nums[i])
        for i in range(n, len(nums)):
            y.append(nums[i])
        
        # Interleave x and y
        result = []
        for i in range(n):
            result.append(x[i])
            result.append(y[i])
        
        return result
