class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        my_list = []
        for i in range(len(words)):
            if x in words[i]:
                my_list.append(i)
        return my_list