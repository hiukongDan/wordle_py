# Implement user interaction and game logic delegation
from controller import Controller
from word_maker import WordMaker
from guess_engine import GuessEngine, GuessStatus
from wordle_solver import WordleSolver
from message import *
import sys

class Wordle:
    def print_help(self):
        print(HELP_MSG)
        
    def print_exit(self):
        print(EXIT_MSG)
        
    def print_newgame(self):
        print(NEW_GAME_MSG)
        
    def print_retry_start(self):
        print(RETRY_START_MSG)
    
    def __init__(self, wordLen=5):
        self.wordLen = wordLen
        self.wordMaker = WordMaker(wordLen)
        self.guessEngine = GuessEngine(self.wordMaker.get_word(), self.wordMaker.get_words())
        self.wordleSolver = WordleSolver(wordLen, self.wordMaker.get_words())
        self.controller = Controller(self.guessEngine, self, self.wordleSolver)
    
    def start(self):
        self.print_help()
        self.print_newgame()
        self.gameloop()
    
    def gameloop(self):
        while(True):
            user_input = input(PROMPT)
            self.controller.process_input(user_input)
            
    def help(self):
        self.print_help()
        
    def exit(self):
        self.print_exit()
        sys.exit(0)
    
    def hint(self, suggestion_word):
        print("Hint suggestion: %s" % suggestion_word)
        
    def newgame(self):
        self.wordMaker.gen_randword()
        self.guessEngine.reset(self.wordMaker.get_word(), self.wordMaker.get_words())
        self.wordleSolver.reset()
        self.print_newgame()
        
    def restart(self):
        self.guessEngine.reset(self.wordMaker.get_word(), self.wordMaker.get_words())
        self.wordleSolver.reset()
        self.print_retry_start()
        
    def solve(self):
        print("word: %s" % self.wordMaker.get_word())
        self.newgame()
    
    def print_guess_result(self, word, result):
        availableAlphabet = self.guessEngine.get_absent_letters_complement()
        print("Try (%d/%d)" % (self.guessEngine.get_total_try(), self.guessEngine.get_max_try()))
        print(" ".join(word))
        print(" ".join(map(lambda x: x.value, result)))
        res = [availableAlphabet[i:i+len(word)] for i in range(0, len(availableAlphabet), len(word))]
        print("Available letters: \n%s" % "\n".join(map(lambda x: " ".join(x), res)))
        
    def suggest_retry(self):
        print(RETRY_MSG)
        
    def win(self):
        print(WIN_MSG)