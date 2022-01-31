#LC2114
# For a list of sentences (each element is a string like so "alice has an apple")
# Find the max number of words in any given sentence

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            words = sentence.split(" ")
            max_words = max(max_words, len(words))
            
        return max_words
      
# To speed this up, don't store things, do it in one line:
# More pythonic anyway :)
class Solution2:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        
        for sentence in sentences:
            max_words = max(max_words, len(sentence.split(" ")))
            
        return max_words
