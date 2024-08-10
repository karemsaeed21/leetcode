class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        answer = ''
        if head is None:
            return 

        temp = head
        while temp is not None:
            answer = answer + str(temp.val)
            temp = temp.next

        return int(answer,2)
        
