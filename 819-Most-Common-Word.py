class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        new_paragraph = ""
        for i in paragraph:
            if i.isalpha() or i == " ":
                new_paragraph += i.lower()
        listed_para = list(new_paragraph.split(" "))
        co = listed_para.count(listed_para[0])
        word = listed_para[0]
        for i in listed_para:
            if i in banned:
                continue
            else:
                if (listed_para.count(i) > co):
                    co = listed_para.count(i)
                    word = i
        return str(word)