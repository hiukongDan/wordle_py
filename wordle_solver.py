import re
import random
from guess_engine import GuessStatus

class WordleSolver:
    def __init__(self, wordLen, words):
        self.wordLen = wordLen
        self.words = words
        self.guesses = []
        self.guesses_status = []
        self.absent_letters = set([])

    def reset(self):
        self.guesses.clear()
        self.guesses_status.clear()
        self.absent_letters = set([])

    def record_guess(self, guess_word, letter_status):
        self.guesses.append(guess_word)
        self.guesses_status.append(letter_status)
        # add absent letters to cache
        for i in range(len(letter_status)):
            if letter_status[i] == GuessStatus.NOT_IN_WORD:
                self.absent_letters.add(guess_word[i])
    
    def absent_complement_letters(self):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = []
        for c in alphabet:
            if c not in self.absent_letters:
                res.append(c)
        return res
        
    def next_suggestion(self):
        if len(self.guesses) == 0:
            return self.words[random.randint(0, len(self.words))]
        absComp = self.absent_complement_letters()
        pattern = ["[%s]"%("".join(absComp))] * self.wordLen
        for i in range(len(self.guesses)):
            for j in range(self.wordLen):
                if self.guesses_status[i][j] == GuessStatus.CORRECT:
                    pattern[j] = self.guesses[i][j]
        regex = re.compile("".join(pattern))
        for word in self.words:
            if regex.match(word):
                return word
        return None