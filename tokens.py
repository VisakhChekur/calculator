from enum import Enum, auto


class TokenType(Enum):

    # Group delimiters.
    LEFT_PARA = auto()  # '('
    RIGHT_PARA = auto()  # ')'

    # Arithmetic operators.
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    EXPONENT = auto()  # '^'

    # Numbers
    NUMBER = auto()


class Token:
    def __init__(
        self, type: TokenType, lexeme: str, column: int, literal: float | int = None
    ):

        self.type = type
        self.lexeme = lexeme
        self.column = column
        self.literal = literal

    def __repr__(self):

        return f"Token({self.type=}, {self.lexeme=}, {self.column=}, {self.literal=}"