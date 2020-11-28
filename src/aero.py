#######################################
# TOKENS
#######################################

TT_INT = 'TT_INT'
TT_FLOAT = 'FLOAT'
TT_PLUS = 'PLUS'
TT_MINUS = 'MINUS'
TT_MUL = 'MUL'
TT_DIV = 'DIV'
TT_LPAREN = 'LPAREN'
TT_RPAREN = 'RPAREN'
TT_EOF = 'EOF'


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
        return f'{self.type}'

#######################################
# LEXER
#######################################


class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None

    def advance(self):
        self.pos += 1
        self.current_char = self.text[self.pos] if self.pos < len(
            self.text) else None

    def make_tokens(self):
        tokens = []

# Mathematical operations and symbol handling/checking by Aero:
        while self.current_char != None:
            if self.current_char in ' \t':
                self.advance()
            elif self.current_char == "+":
                tokens.append(Token(TT_PLUS))
                self.advance()
            elif self.current_char == "-":
                tokens.append(Token(TT_MINUS))
                self.advance()
            elif self.current_char == "*":
                tokens.append(Token(TT_MUL))
                self.advance()
            elif self.current_char == "/":
                tokens.append(Token(TT_DIV))
                self.advance()
            elif self.current_char = ="(":
                tokens.append(Token(TT_LPAREN))
                self.advance()
            elif self.current_char == ")":
                tokens.append(Token(TT_RPAREN))
                self.advance()

        return tokens
