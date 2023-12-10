from typing import TypeVar
from typing import ParamSpec

from lambda_lite.typedefs import MonadicFunction
from lambda_lite.typedefs import DyadicFunction
from lambda_lite.typedefs import VariadicFunction

_A = TypeVar("_A")
_B = TypeVar("_B")
_C = TypeVar("_C")
_D = TypeVar("_D")
_P = ParamSpec("_P")


def compose(f: MonadicFunction[_B, _C], g: VariadicFunction[_P, _B]) -> VariadicFunction[_P, _C]:
    def h(*args: _P.args, **kwargs: _P.kwargs) -> _C:
        if args or kwargs:
            return f(g(*args, **kwargs))
        return f(g())

    return h


def flip_(f: DyadicFunction[_A, _B, _C]) -> DyadicFunction[_B, _A, _C]:
    def flipped(b: _B, a: _A) -> _C:
        return f(a, b)

    return flipped


def id_(x: _A) -> _A:
    """Identity combinator.

    λa.a

    """
    return x


def const_(a: _A, b: _B) -> _A:
    """K combinator.

    λab.a

    """
    return a


def join_(f: DyadicFunction[_A, _A, _B]) -> MonadicFunction[_A, _B]:
    def inner(a: _A) -> _B:
        return f(a, a)

    return inner


def s(f: DyadicFunction[_A, _B, _C], g: MonadicFunction[_A, _B]) -> MonadicFunction[_A, _C]:
    def inner(x: _A) -> _C:
        return f(x, g(x))

    return inner


def on_(
        f: DyadicFunction[_B, _B, _C],
        g: MonadicFunction[_A, _B],
        a: _A,
        b: _A) -> _C:
    """psi combinator"""
    return f(g(a), g(b))


def applicator(f: MonadicFunction[_A, _B], a: _A) -> _B:
    """i-star combinator"""
    return f(a)


def becard_(f: MonadicFunction[_C, _D], g: MonadicFunction[_B, _C], h: MonadicFunction[_A, _B], a: _A) -> _D:
    """B3 combinator"""
    return f(g(h(a)))


def blackbird_(f: MonadicFunction[_C, _D], g: DyadicFunction[_A, _B, _C], a: _A, b: _B) -> _D:
    return f(g(a, b))


__all__ = ["compose", "flip_", "id_", "join_", "s"]
