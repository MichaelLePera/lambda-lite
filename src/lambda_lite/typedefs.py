from typing import Callable
from typing import TypeVar
from typing import ParamSpec
from typing import TypeAlias


_A = TypeVar("_A")
_B = TypeVar("_B")
_C = TypeVar("_C")
_D = TypeVar("_D")
_P = ParamSpec("_P") 


NiladicFunction: TypeAlias = Callable[[], _B]
MonadicFunction: TypeAlias = Callable[[_A], _B]
DyadicFunction: TypeAlias = Callable[[_A, _B], _C]
ParametricFunction: TypeAlias = Callable[_P, _B]
Predicate: TypeAlias = Callable[..., bool]
VariadicFunction: TypeAlias = Callable[_P, _B]

__all__ = [
    "NiladicFunction",
    "MonadicFunction",
    "DyadicFunction",
    "ParametricFunction",
    "Predicate",
    "VariadicFunction",

]

