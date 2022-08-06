class SyntaxError(Exception):
    def __init__(self, message, column):
        print(f"SyntaxError: {message} at column {column}")


class ParseError(Exception):
    def __init__(self, message, column):
        print(f"PareError: {message} at column {column}")
