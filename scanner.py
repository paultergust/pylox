from .token_type import TokenType
from .token import Token


class Scanner:

    def __init__(self, src):
        self._src = src
        self._tokens = []
        self._start = 0
        self._current = 0
        self._line = 0

    def scan_tokens(self):
        while not self.is_at_end():
            self._start = self._current
            self.scan_token()

        self._tokens.append(Token(TokenType.EOF, '', None, self._line))
        return self._tokens

    def is_at_end(self):
        return self._current >= len(self._src)

    def scan_token(self):
        c = self.advance()
        match c:
            case '(':
                self.add_token(TokenType.LEFT_PAREN)
            case ')':
                self.add_token(TokenType.RIGHT_PAREN)
            case '{':
                self.add_token(TokenType.LEFT_BRACE)
            case '}':
                self.add_token(TokenType.RIGHT_BRACE)
            case ',':
                self.add_token(TokenType.COMMA)
            case '.':
                self.add_token(TokenType.DOT)
            case '-':
                self.add_token(TokenType.MINUS)
            case '+':
                self.add_token(TokenType.PLUS)
            case ';':
                self.add_token(TokenType.SEMICOLON)
            case '*':
                self.add_token(TokenType.STAR)

    def advance(self):
        return self._src[self._current + 1]

    def add_token(self, token_type, literal=None):
        text = self._src[self._start, self._current]
        self._tokens.append(Token(token_type, text, literal, self._line))
