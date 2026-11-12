
import sys
from antlr4 import *
from antlr4.error.ErrorListener import ErrorListener

from Deliverable1Lexer import Deliverable1Lexer
from Deliverable1Parser import Deliverable1Parser


class ParseErrorListener(ErrorListener):
    def __init__(self):
        super().__init__()
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol,
                    line, column, msg, e):
        self.errors.append(f"Line {line}:{column} - {msg}")


def main():
    if len(sys.argv) < 2:
        print("Usage: py main.py <input_file>")
        return

    input_stream = FileStream(sys.argv[1], encoding="utf-8")

    lexer = Deliverable1Lexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = Deliverable1Parser(token_stream)

    error_listener = ParseErrorListener()
    lexer.removeErrorListeners()
    parser.removeErrorListeners()
    lexer.addErrorListener(error_listener)
    parser.addErrorListener(error_listener)

    tree = parser.program()

    if error_listener.errors:
        print("Syntax errors found:")
        for error in error_listener.errors:
            print(error)
    else:
        print("Syntax valid!")
        print("Parse tree:")
        print(tree.toStringTree(recog=parser))


if __name__ == "__main__":
    main()
