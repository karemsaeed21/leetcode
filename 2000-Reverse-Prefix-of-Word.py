class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        if ch in word:
            ind = word.index(ch)
        else:
            return "".join(word)

        return "".join(word[:ind+1][::-1]) + "".join(word[ind+1:])