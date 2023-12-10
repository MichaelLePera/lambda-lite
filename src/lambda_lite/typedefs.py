from typing import Callable

type NiladicFunction[B] = Callable[[], B]
type MonadicFunction[A, B] = Callable[[A], B]
type DyadicFunction[A, B, C] = Callable[[A, B], C]
type ParametricFunction[**P, B] = Callable[P, B]
type Predicate = Callable[..., bool]
type VariadicFunction[B] = Callable[..., B]


__all__ = [
    "NiladicFunction",
    "MonadicFunction",
    "DyadicFunction",
    "ParametricFunction",
    "Predicate",
    "VariadicFunction",

]

