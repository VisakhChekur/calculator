from abc import ABC, abstractmethod


class Expr(ABC):
    @abstractmethod
    def accept(self):
        pass


class Literal(Expr):
    pass


class Unary(Expr):
    pass


class Binary(Expr):
    pass


class Grouping(Expr):
    pass
