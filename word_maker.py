# Implement legal word generation
from english_words import english_words_lower_alpha_set
import random

class WordMaker:
    def __init__(self, wordlen):
        self.wordlen = wordlen
        self.filter_words(wordlen)
        self.word = ""
        
    def filter_words(self, wordlen):
        self.words = []
        for w in english_words_lower_alpha_set:
            if len(w) == wordlen:
                self.words.append(w)
                
    def gen_randword(self):
        self.word = self.words[random.randint(0, len(self.words)-1)]
    
    
    def get_word(self):
        if self.word == "":
            self.gen_randword()
        return self.word
        
        
    def get_words(self):
        return self.words
        