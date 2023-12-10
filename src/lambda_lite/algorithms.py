from typing import TypeVar
from typing import ParamSpec
from typing import Iterable
from typing import Generator

from lambda_lite.typedefs import DyadicFunction
from lambda_lite.typedefs import MonadicFunction
from lambda_lite.typedefs import Predicate


_A = TypeVar("_A")
_B = TypeVar("_B")
_C = TypeVar("_C")
_D = TypeVar("_D")
_P = ParamSpec("_P")


def foldl(f: DyadicFunction[_B, _A, _B], z: _B, xs: Iterable[_A]) -> _B:
    acc = z
    for x in xs:
        acc = f(acc, x)
    return acc


def foldl1(f: DyadicFunction[_A, _A, _A], xs: Iterable[_A]) -> _A:
    """Assume non empty.
    """
    tail = iter(xs)
    head = next(tail)
    return foldl(f, head, tail)


def map(f: MonadicFunction[_A, _B], xs: Iterable[_A]) -> Generator[_B, None, None]:
    for x in xs:
        yield f(x)


def filter(f: Predicate[_A], xs: Iterable[_A]) -> Generator[_A, None, None]:
    for x in xs:
        if f(x):
            yield x
