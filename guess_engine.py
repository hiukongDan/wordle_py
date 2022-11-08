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
    CORRECT = 1
    IN_WORD = 2
    NOT_IN_WORD = 3

class GuessEngine:
    def __init__(self, word, words):
        self.reset(word, words)
        
    def reset(self, word, words):
        self.word = word
        self.words = words
        self.guesses = []
        self.absentLetters = set([])
    
    def guess(self, guess):
        if guess not in self.words:
            print ("Not a word!: %s" % guess)
            return []
        if len(guess) != len(self.word):
            print("Not correct length! should have: %d" % len(self.word))
            return []
            
        self.guesses.append(guess)
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
        
    def get_absentLetters(self):
        return list(self.absentLetters)