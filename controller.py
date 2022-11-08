# Implement delegate user input to game logic facility
from word_maker import WordMaker
from guess_engine import GuessEngine, GuessStatus
from input_processor import InputProcessor, InputType

class Controller:
    def __init__(self, guessEngine, wordle, wordleSolver):
        self.guessEngine = guessEngine
        self.inputProcessor = InputProcessor()
        self.wordle = wordle
        self.wordleSolver = wordleSolver
        
    def process_input(self, input):
        input = input.strip().lower()
        type = self.inputProcessor.process_input(input)
        if type == InputType.INVALID:
            print("invalid input: %s" % input)
        elif type == InputType.WORD:
            res = self.guessEngine.guess(input)
            if res == []: return
            self.wordle.print_guess_result(input, res)
            self.wordleSolver.record_guess(input, res)
            if not self.guessEngine.can_try():
                self.wordle.suggest_retry()
            elif all(map(lambda x: x == GuessStatus.CORRECT, res)):
                self.wordle.win()
                self.wordle.newgame()
        elif type == InputType.COMMAND_HELP:
            self.wordle.help()
        elif type == InputType.COMMAND_EXIT:
            self.wordle.exit()
        elif type == InputType.COMMAND_HINT:
            suggestion_word = self.wordleSolver.next_suggestion()
            self.wordle.hint(suggestion_word)
        elif type == InputType.COMMAND_RESTART:
            # do restart
            self.wordle.restart()
        elif type == InputType.COMMAND_NEW:
            self.wordle.newgame()
        elif type == InputType.COMMAND_SOLVE:
            # do solve
            self.wordle.solve()