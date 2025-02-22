class Solution(object):
    def plusOne(self, digits):
        digits = ''.join(map(str, digits))
        digits = str(int(digits) + 1)
        return [int(x) for x in digits]
        # digit = \\
        # for x in digits:
        #     digit += str(x)
        # digit = str(int(digit) + 1)
        # l = []
        # for x in digit:
        #     l.append(int(x))
        # return l