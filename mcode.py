from lexer import Lexer
from parse import Parse
from evaluator import Evaluator

def main():
    filename = 'coinToss.mc'
    file     =  open(filename, 'r')
    lexer    = Lexer(file)
    parse   = Parse(lexer.tokens)

    lexer.tokenizer()
    print("Tokens:")
    print(lexer.tokens, "\n")

    parse.build_AST()
    print("AST:")
    print(parse.AST, "\n")

    evaluator = Evaluator(parse.AST)
    print("OUTPUT:")
    evaluator.run(parse.AST)

if __name__ == "__main__":
    main()