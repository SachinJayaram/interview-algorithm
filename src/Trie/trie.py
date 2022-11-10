#!/usr/bin/env python

class Trie:
    def __init__(self) -> None:
        """!
        Trie Initializer
        """
        self.head = {}

    def insert(self, word):
        """!
        Inserts a word into the trie.
        """
        head = self.head
        for ch in word:
            if ch not in head:
                head[ch] = {}
            head = head[ch]
        head['*'] = True

    def search(self, word):
        """!
        Returns if the word is in the trie.
        """
        head = self.head
        for ch in word:
            if ch not in head:
                return False
            head = head[ch]
        
        return '*' in head

    def starts_with(self, prefix):
        """!
        Returns if there is any word in the trie
        that starts with the given prefix.
        """
        head = self.head
        for ch in prefix:
            if ch not in head:
                return False
            head = head[ch]

        return True


def main():
    trie = Trie()
    trie.insert('Sachin')
    trie.insert('Jayaram')
    print('Sachin in Trie? {0}'.format(trie.search('Sachin')))
    print('Jayaram in Trie? {0}'.format(trie.search('Jayaram')))
    print('Miti in Trie? {0}'.format(trie.search('Miti')))


if __name__ == '__main__':
    main()