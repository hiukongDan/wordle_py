import re
import random
from guess_engine import GuessStatus

class WordleSolver:
    def __init__(self, wordLen, words):
        self.wordLen = wordLen
        self.words = words
        self.reset()
        
    def reset(self):
        self.guesses = []
        self.guesses_status = []
        self.absent_letters = [set([]) for i in range(self.wordLen)]
        self.present_letters = set([])
        self.correct_letters = [" "] * self.wordLen
        self.hint_history = []

    def record_guess(self, guess_word, letter_status):
        self.guesses.append(guess_word)
        self.guesses_status.append(letter_status)
        self.hint_history = []
        # add absent letters to cache
        for i in range(len(letter_status)):
            #print("%d: %s" % (i, letter_status[i]))
            if letter_status[i] == GuessStatus.NOT_IN_WORD:
                for j in range(self.wordLen):
                    self.absent_letters[j].add(guess_word[i])
            elif letter_status[i] == GuessStatus.IN_WORD:
                self.present_letters.add(guess_word[i])
                self.absent_letters[i].add(guess_word[i])
            elif letter_status[i] == GuessStatus.CORRECT:
                self.present_letters.add(guess_word[i])
                self.correct_letters[i] = guess_word[i]
    
    def absent_complement_letters(self):
        return self.alphabet_complement(self.absent_letters)
        
    def alphabet_complement(self, letter_set):
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        res = []
        for c in alphabet:
            if c not in letter_set:
                res.append(c)
        return res
        
    def build_regex_string_for_index(self, i):
        if i < 0 or i >= self.wordLen: return ""
        if self.correct_letters[i] != " ": return self.correct_letters[i]
        possible = self.alphabet_complement(list(self.absent_letters[i]))
        # print("possible for %d: %s" % (i, "[%s]" % ("".join(possible))))
        return "[%s]" % ("".join(possible))
        
    def next_suggestion(self):
        if len(self.guesses) == 0:
            return self.words[random.randint(0, len(self.words))]
        # build regex for each letter
        pattern = ""
        for i in range(self.wordLen):
            pattern += self.build_regex_string_for_index(i)
            
        regex = re.compile(pattern)
        for word in self.words:
            if word in self.hint_history:
                continue
            if regex.match(word):
                if (self.present_letters & set([*word])) == self.present_letters:
                    self.hint_history.append(word)
                    return word
        return None