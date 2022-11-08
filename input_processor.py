from enum import Enum

class InputType(Enum):
    WORD            = 1
    COMMAND_HELP    = 2
    COMMAND_EXIT    = 3
    COMMAND_HINT    = 4
    COMMAND_RESTART = 5
    COMMAND_SOLVE   = 6
    COMMAND_NEW     = 7
    INVALID         = 8
    

class InputProcessor:
    def __init__(self):
        pass
    
    def process_input(self, input):
        if len(input) == 0: return InputType.INVALID
        if input[0] == '/': return self.process_command(input[1:])
        else: return self.process_word(input)
        
    def process_command(self, cmd):
        if (cmd == "help"): return InputType.COMMAND_HELP
        if (cmd == "exit"): return InputType.COMMAND_EXIT
        if (cmd == "hint"): return InputType.COMMAND_HINT
        if (cmd == "restart"): return InputType.COMMAND_RESTART
        if (cmd == "new"): return InputType.COMMAND_NEW
        if (cmd == "solve"): return InputType.COMMAND_SOLVE
        
        return InputType.INVALID
        
        
    def process_word(self, input):
        return InputType.WORD if input.isalpha() else InputType.INVALID
    
    