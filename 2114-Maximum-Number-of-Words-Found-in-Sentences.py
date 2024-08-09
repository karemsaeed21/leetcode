class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        ma = 0
        spl = ""
        for i in range(len(sentences)):
            spl = ""
            for j in range(len(sentences[i])):
                spl = sentences[i].split()
            ma = max(ma,len(spl))

        return ma

        
        