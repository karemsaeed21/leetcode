class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        return sum(1 for i in words if i.startswith(pref))   