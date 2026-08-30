class WordDictionary:

    def __init__(self):
        self.trie = {}

    def addWord(self, word: str) -> None:
        d = self.trie

        for char in word:
            if char not in d:
                d[char] = {}
            d = d[char]
        
        d[','] = ','

    def helpSearch(self, word, d) -> bool:
        
        for i,char in enumerate(word):
            if char == ".":
                for child in d:
                    if child != "," and self.helpSearch(word[i+1:],d = d[child]):
                        return True
                return False

            if char not in d:
                return False

            d = d[char]
        return "," in d

    def search(self, word: str) -> bool:
        return self.helpSearch(word, self.trie)

        
