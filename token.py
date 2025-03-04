from .token_type import TokenType


class Token:

    def __init__(self, _type: TokenType, lexeme, literal, line):
        self._type = _type
        self._lexeme = lexeme
        self._literal = literal
        self._line = line

    def __str__(self):
        return self._type + ' ' + self._lexeme + ' ' + self._literal
