class TrieNode():
    def __init__(self):
        self.characters={}
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        
    def addWord(self, word: str) -> None:
        curr = self.root
        for w in word:
            if w not in curr.characters:
                curr.characters[w] = TrieNode()
            curr = curr.characters[w]
        curr.endOfWord = True

    def search(self, word: str) -> bool:
        def dfs(j, node):
            curr = node
            for i in range(j, len(word)):
                c = word[i]
                if c==".":
                    for value in curr.characters.values():
                        if dfs(i+1, value):
                            return True
                    return False
                else:
                    if c not in curr.characters:
                        return False
                    curr = curr.characters[c]
            return curr.endOfWord
        return dfs(0, self.root)