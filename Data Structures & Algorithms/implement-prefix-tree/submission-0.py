class Trie:
    def __init__(self):
        self.children={}
        self.end=False
class PrefixTree:

    def __init__(self):
        self.root=Trie()

    def insert(self, word: str) -> None:
        cur=self.root
        for c in word:
            if c not in cur.children:
                cur.children[c]=Trie()
            cur=cur.children[c]
        cur.end=True

    def search(self, word: str) -> bool:
        cur = self.root
        for c in word:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        if(cur.end==True):
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        cur = self.root
        for c in prefix:
            if c not in cur.children:
                return False
            cur=cur.children[c]
        return True
        