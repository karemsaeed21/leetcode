class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        total = defaultdict(int)
        for value, weight in items1 + items2:
            total[value] += weight

        return [[key, total[key]] for key in sorted(total)]