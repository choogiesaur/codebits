# Implement a version of a Trie where words are terminated with '*'
# Efficient space complexity vs hashtable
# Acceptable time complexity. O(Key_Length) for insert/find
# Handle edge cases:
# - Empty String
# - Contains non alphabet characters (numbers or symbols)
# - Case sensitivity

class StarTrie:
    # Each node has a dictionary of its children
    head = {}
    
    def add(self, word):
        curr = self.head
        
        for ch in word:
            if ch not in curr:
                # Make a new children dict
                curr[ch] = {}
            # Traverse downward
            curr = curr[ch]
        # Terminate word by storing '*' as a child
        curr['*'] = {}
        
    def search(self, word):
        curr = self.head
        
        for ch in word:
            if ch not in curr:
                return False
            curr = curr[ch]
            
        if '*' not in curr:
            return False
        else:
            return True

my_trie = StarTrie()

test_str = "hello welcome to hell have some jello"
for word in test_str.split():
    my_trie.add(word)

print(my_trie.head)
print(my_trie.search('hello'))
print(my_trie.search('hell'))
print(my_trie.search('hel'))
print(my_trie.search('welcome'))
print(my_trie.search('jello'))
print(my_trie.search(''))

my_trie.add('')
print(my_trie.search(''))
