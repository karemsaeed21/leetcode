class Solution:
        def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
            counter = 0
            n = len(tickets)
            while tickets[k] > 0:
                for i in range(n):
                    if tickets[i] > 0:
                        tickets[i] -= 1
                        counter += 1
                    if tickets[k] == 0: break
            return counter