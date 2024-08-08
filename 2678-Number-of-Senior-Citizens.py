class Solution:
    def countSeniors(self, details: List[str]) -> int:
        return sum(info[11] > '6' or (info[11] == '6' and info[12] > '0') for info in details)