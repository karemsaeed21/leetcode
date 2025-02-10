class Solution(object):
    def convertDateToBinary(self, date):
        new_date = map(int,date.split("-"))
        binary_date = [bin(part)[2:] for part in new_date]
        return "-".join(binary_date)
        