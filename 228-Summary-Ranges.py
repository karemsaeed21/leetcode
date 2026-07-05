class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        output = []
        final = []

        if not nums:
            return []

        for i in range(len(nums)):
            if i == 0:
                output.append(nums[i])
            else:
                if nums[i] - 1 == nums[i - 1]:
                    output.append(nums[i])
                else:
                    output.append("split")
                    output.append(nums[i])

        current = []

        for item in output:
            if item != "split":
                current.append(item)
            else:
                if len(current) == 1:
                    final.append(str(current[0]))
                else:
                    final.append(f"{current[0]}->{current[-1]}")
                current = []

        if current:
            if len(current) == 1:
                final.append(str(current[0]))
            else:
                final.append(f"{current[0]}->{current[-1]}")

        return final