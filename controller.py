# Implement delegate user input to game logic facility
from word_maker import WordMaker
from guess_engine import GuessEngine, GuessStatus
from input_processor import InputProcessor, InputType

class Controller:
    def __init__(self, guessEngine, wordle):
        self.guessEngine = guessEngine
        self.inputProcessor = InputProcessor()
        self.wordle = wordle
        
    def process_input(self, input):
        input = input.strip()
        type = self.inputProcessor.process_input(input)
        if type == InputType.INVALID:
            print("invalid input: %s" % input)
        elif type == InputType.WORD:
            res = self.guessEngine.guess(input)
        elif type == InputType.COMMAND_HELP:
            self.wordle.help()
        elif type == InputType.COMMAND_EXIT:
            self.wordle.exit()
        elif type == InputType.COMMAND_HINT:
            # do hint
            self.wordle.hint()
        elif type == InputType.COMMAND_RESTART:
            # do restart
            self.wordle.restart()
        elif type == InputType.COMMAND_SOLVE:
            # do solve
            self.wordle.solve()