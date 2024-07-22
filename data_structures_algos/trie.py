class TrieNode:

    def __init__(self):
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def search(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                return None
        
        return currentNode
    
    def insert(self, word):
        currentNode = self.root

        for char in word:
            if currentNode.children.get(char):
                currentNode = currentNode.children[char]
            else:
                newNode = TrieNode()
                currentNode.children[char] = newNode
                currentNode = newNode
        currentNode.children["*"] = None

    def collectAllWords(self, node=None, word="", words=[]):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            if key == "*":
                words.append(word)
            else:
                self.collectAllWords(childNode, word + key, words)
        return words
    
    def autocomplete(self, prefix):
        currentNode = self.search(prefix)
        if not currentNode:
            return None
        return self.collectAllWords(currentNode)
    
    def print_nodes(self, node=None):
        currentNode = node or self.root

        for key, childNode in currentNode.children.items():
            print(key)
            if key != "*":
                self.print_nodes(childNode)