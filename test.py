import unittest
from word_maker import WordMaker
from guess_engine import GuessEngine, GuessStatus
from input_processor import InputProcessor, InputType


class WordleTest(unittest.TestCase):
    def test_word_maker(self):
        wordMaker = WordMaker(5)
        word = wordMaker.get_word()
        self.assertEqual(5, len(word))
        
    def test_guess_engine(self):
        wordMaker = WordMaker(5)
        word = wordMaker.get_word()
        words = wordMaker.get_words()
        
        guessEngine = GuessEngine("world", words)
        self.assertEqual(guessEngine.get_absentLetters(), [])
        
        self.assertEqual([], guessEngine.guess("abcde"))
        
        res = guessEngine.guess("world")
        self.assertEqual(res, [GuessStatus.CORRECT,
            GuessStatus.CORRECT, GuessStatus.CORRECT, GuessStatus.CORRECT, GuessStatus.CORRECT])
        
        
        guessEngine.reset("world", words)
        res = guessEngine.guess("whole")
        self.assertEqual(res, [GuessStatus.CORRECT,
            GuessStatus.NOT_IN_WORD, GuessStatus.IN_WORD, GuessStatus.CORRECT, GuessStatus.NOT_IN_WORD])
    
    def test_input_processor(self):
        inputProcessor = InputProcessor()
        self.assertEqual(InputType.WORD, inputProcessor.process_input("world"))
        self.assertEqual(InputType.COMMAND_HELP, inputProcessor.process_input("/help"))
        self.assertEqual(InputType.COMMAND_EXIT, inputProcessor.process_input("/exit"))
        self.assertEqual(InputType.COMMAND_HINT, inputProcessor.process_input("/hint"))
        self.assertEqual(InputType.COMMAND_RESTART, inputProcessor.process_input("/restart"))
        self.assertEqual(InputType.COMMAND_SOLVE, inputProcessor.process_input("/solve"))
        self.assertEqual(InputType.INVALID, inputProcessor.process_input("/unknownCommand"))
        self.assertEqual(InputType.INVALID, inputProcessor.process_input("worl3d"))
        self.assertEqual(InputType.INVALID, inputProcessor.process_input("/exit_"))
        


if __name__ == "__main__":
    unittest.main()