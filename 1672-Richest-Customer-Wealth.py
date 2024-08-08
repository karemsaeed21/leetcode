class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        temp = sums = 0
        for i in range(len(accounts)):
            sums = 0
            for j in range(0,len(accounts[i])):
                sums += accounts[i][j]
            temp = max(temp,sums)

        return temp
        