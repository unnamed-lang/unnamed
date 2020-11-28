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
    def __init__(self, type_, _value):
        self.type_ = type_
        self._value = _value

    def __repr__(self):
        if self.value:
            return f'{self.type}:{self.value}'
            return f'{self.type}'
