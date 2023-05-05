# The flux templating "language". v0.1.0-beta
# https://github.com/blaze0x0/flux
import os

try:
    import readline
except ImportError:
    readline = None
    
class Flux:
    def __init__(self, text):
        self.text = text
        self.idx  = -1
        self.max_idx = len(text)-1
        self.cur = None
        self.advance()

    def reset(self, text):
        self.idx = -1
        self.max_idx = len(text) - 1
        self.text = text
        self.cur = None
        self.advance()

    def advance(self):
        self.idx += 1
        try:
            self.cur = self.text[self.idx]
        except IndexError:
            self.cur = '\n'

    def parse(self, args={}):
        parsed = ""
        while self.idx <= self.max_idx:
            if self.cur == '<' and self.text[self.idx:self.idx+4] == "<<<<":
                self.idx += 3
                self.advance()
                variable = self.complete(">")
                value = self.evaluate(variable, args)
                parsed += str(value)
                self.idx += 2
                self.advance()
            else:
                parsed += self.cur
            self.advance()
        return parsed

    def complete(self, stop_char):
        text = ""
        while self.idx <= self.max_idx:
            if self.cur == stop_char and self.text[self.idx:self.idx+4] == stop_char * 4:
                break
            text += self.cur
            self.advance()
        return text
        
    def evaluate(self, expr, args):
        if expr in args:
            return args[expr]
        operators = {
                    "**": lambda x, y: x**y,
                    "*": lambda x, y: x*y,
                    "/": lambda x, y: x/y if y != 0 else "undefined",
                    "+": lambda x, y: x+y,
                    "-": lambda x, y: x-y
        }
        for operator in operators.keys():
            if operator in expr:
                operands = expr.split(operator)
                break
        else:
            return "undefined"
        try:
            operand1 = int(operands[0]) if "." not in operands[0] else float(operands[0])
            operand2 = int(operands[1]) if "." not in operands[1] else float(operands[1])
        except:
            return "undefined"
        return operators[operator](operand1, operand2)
        

def parse_text(text :str, args : dict):
    flux = Flux(text)
    parsed = flux.parse(args)
    return parsed

def parse_file(filename : str, args : dict):
    if not os.path.exists(filename):
        raise FileNotFoundError(f"Requested file not found: {filename}")
    with open(filename, "r") as f:
        parsed = parse_text(f.read(), args)
    return parsed


# Flux "Interpreter"
if __name__ == "__main__":
    print("Flux v0.1.0-beta (by blaze0x0)")
    print("This project is in development. Please report any issues at the github repository.")
    print("Running Flux as main...")
    while True:
        try:
            text = input("\033[0;38;5;214mflux\033[0m > ")
        except KeyboardInterrupt:
            print("\n")
            break
        flux = Flux(text)
        parsed = flux.parse({}) # IDK why i did this
        print(parsed)
