# Local imports.
from tokens import Token, TokenType
from errrors import SyntaxError


class Scanner:
    def __init__(self, expression: str = ""):

        self.expression = expression
        self._current = self._start = 0
        self._tokens: list[Token] = []

    def scan(self):

        try:
            while self._current < len(self.expression):
                self._start = self._current
                self._scan_char()
            return self._tokens
        except SyntaxError:
            return []

    def _scan_char(self):

        c = self._advance()
        match c:

            case "(":
                self._add_token(TokenType.LEFT_PARA)
            case ")":
                self._add_token(TokenType.RIGHT_PARA)
            case "+":
                self._add_token(TokenType.PLUS)
            case "-":
                self._add_token(TokenType.MINUS)
            case "*":
                self._add_token(TokenType.STAR)
            case "/":
                self._add_token(TokenType.SLASH)
            case "^":
                self._add_token(TokenType.EXPONENT)
            case ".":
                raise SyntaxError("Numbers can not start with '.'", self._current)
            case " ":
                pass
            case _:
                if c.isdigit():
                    self._handle_number()
                else:
                    raise SyntaxError(
                        f"Uncrecognized character '{self._current - 1}'",
                        self._current,
                    )

    def _handle_number(self) -> None:

        while not self._is_at_end() and self._peek().isdigit():
            self._advance()

        # Handles the decimal portion of the number if it exists.
        if self._peek() == ".":
            self._advance()
            while not self._is_at_end() and self._peek().isdigit():
                self._advance()

        num_str = self.expression[self._start : self._current]
        num = int(num_str) if num_str.isdigit() else float(num_str)
        self._add_token(TokenType.NUMBER, num)

    def _is_at_end(self):
        """Returns True if the end of the expression has been reached."""
        return self._current >= len(self.expression)

    def _peek(self) -> str:
        """Returns the current character WITHOUT consuming it."""
        return self.expression[self._current]

    def _advance(self) -> str:
        """Consumes the current character and returns the consumed character."""

        self._current += 1
        return self.expression[self._current - 1]

    def _add_token(self, type, literal=None) -> None:

        lexeme = self.expression[self._start : self._current]
        new_token = Token(type, lexeme, self._start, literal)
        self._tokens.append(new_token)
