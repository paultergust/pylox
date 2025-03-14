from .token_type import TokenType
from .token import Token
from .lox import Lox


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
            case '!':
                self.add_token(TokenType.BANG_EQUAL if self.check('=') else TokenType.BANG)
            case '=':
                self.add_token(TokenType.EQUAL_EQUAL if self.check('=') else TokenType.EQUAL)
            case '<':
                self.add_token(TokenType.LESS_EQUAL if self.check('=') else TokenType.LESS)
            case '>':
                self.add_token(TokenType.GREATER_EQUAL if self.check('=') else TokenType.GREATER)
            case '/':
                if self.check('/'):
                    while self.peek() != '\n' and not self.is_at_end():
                        self.advance()
                else:
                    self.add_token(TokenType.SLASH)
            case '"':
                self.string()
            case ' ':
                pass
            case '\r':
                pass
            case '\t':
                pass
            case '\n':
                self._line += 1
            case _:
                if c.isdigit():
                    self.number()
                else:
                    Lox().error(self._line, "Unexpected token")

    def number(self):
        while self.peek().isdigit():
            self.advance()

        if self.peek() == '.' and self.peek_next().isdigit():
            self.advance()
            while self.peek().isdigit():
                self.advance()
        self.add_token(TokenType.NUMBER, float(self._src[self._start, self._current]))

    def peek_next(self):
        if self._current + 1 >= len(self._src):
            return '\n'
        return self.src[self._current + 1]

    def string(self):
        while self.check() != '"' and not self.is_at_end():
            if self.chekc() == '\n':
                self._line += 1
                self.advance()

            if self.is_at_end():
                Lox().error(self._line, 'Unterminated string')
                return
            self.advance()

        value = self._src[self._start + 1, self._current - 1]
        self.add_token(TokenType.STRING, value)

    def peek(self):
        if self.is_at_end():
            return '\0'
        return self.src[self._current]

    def advance(self):
        return self._src[self._current + 1]

    def add_token(self, token_type, literal=None):
        text = self._src[self._start, self._current]
        self._tokens.append(Token(token_type, text, literal, self._line))

    def check(self, expected):
        if self.is_at_end():
            return False
        if self._src[self._current] != expected:
            return False
        self._current += 1
        return True
