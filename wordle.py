# Implement user interaction and game logic delegation
from controller import Controller
from word_maker import WordMaker
from guess_engine import GuessEngine, GuessStatus
from message import *
import sys

class Wordle:
    def print_help(self):
        print(HELP_MSG)
        
    def print_exit(self):
        print(EXIT_MSG)
        
    def print_newgame(self):
        print(NEW_GAME_MSG)
    
    def __init__(self):
        self.wordMaker = WordMaker(5)
        self.guessEngine = GuessEngine(self.wordMaker.get_word(), self.wordMaker.get_words())
        self.controller = Controller(self.guessEngine, self)
    
    def start(self):
        self.print_help()
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
    
    def hint(self):
        print("Hint: ")
        
    def restart(self):
        self.wordMaker.gen_randword()
        self.guessEngine.reset(self.wordMaker.get_word(), self.wordMaker.get_words())
        self.print_newgame()
        
    def solve(self):
        print("solved!")
        self.restart()
    
        
        