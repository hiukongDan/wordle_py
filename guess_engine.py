# Implement word guessing assisting facility
from english_words import english_words_lower_alpha_set
from word_maker import WordMaker
from enum import Enum
"""
When player enter a word, the game interface print error if the input is not an english word.
When player enter a legal word, the interface print how many letters are correct, the letters
in the word if user entered and letters not in the word.
"""

"""
Responsibility of GuessEngine
1. compare user input and correct answer
2. compute letter status given user input
3. record used letters
"""


class GuessStatus(Enum):
    CORRECT = "v"
    IN_WORD = "?"
    NOT_IN_WORD = "x"

class GuessEngine:
    def __init__(self, word, words):
        self.reset(word, words)
        self.totalTry = 0
        self.maxTry = 6
        
    def reset(self, word, words):
        self.word = word
        self.words = words
        self.guesses = []
        self.absentLetters = set([])
        self.totalTry = 0
    
    def guess(self, guess):
        if guess not in self.words:
            print ("Not a word in data range!: %s" % guess)
            return []
        if len(guess) != len(self.word):
            print("Not correct length! should have: %d" % len(self.word))
            return []
        if not self.can_try():
            print("You can't try more!")
            return []
        
        self.guesses.append(guess)
        self.totalTry += 1
        res = []
        for i in range(len(guess)):
            if guess[i] == self.word[i]:
                res.append(GuessStatus.CORRECT)
            elif guess[i] in self.word:
                res.append(GuessStatus.IN_WORD)
            else:
                res.append(GuessStatus.NOT_IN_WORD)
                self.absentLetters.add(guess[i])
        return res
        
    def get_absent_letters(self):
        return list(self.absentLetters)
        
    def get_absent_letters_complement(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = []
        for c in alphabet:
            if c not in self.absentLetters:
                res.append(c)
        return res
        
    def can_try(self):
        return self.totalTry < self.maxTry;
        
    def get_max_try(self):
        return self.maxTry
    
    def get_total_try(self):
        return self.totalTry
        
    def get_word_length(self):
        return len(self.word)