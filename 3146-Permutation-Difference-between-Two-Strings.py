class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        indices_s = {char: index for index, char in enumerate(s)}
        indices_t = {char: index for index, char in enumerate(t)}
        permutation_difference = 0
        
        for char in s:
            permutation_difference += abs(indices_s[char] - indices_t[char])
        
        return permutation_difference