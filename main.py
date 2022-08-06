from scanner import Scanner
from errrors import SyntaxError, ParseError

valid = "1 + 2 - 4.5"

invalid = ".80"


scanner = Scanner(valid)
try:
    tokens = scanner.scan()
except SyntaxError:
    pass
except ParseError:
    pass
