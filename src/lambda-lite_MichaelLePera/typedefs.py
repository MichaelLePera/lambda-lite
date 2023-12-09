from typing import Callable

type NiladicFunction[B] = Callable[[], B]
type MonadicFunction[A, B] = Callable[[A], B]
type DyadicFunction[A, B, C] = Callable[[A, B], C]
type ParametricFunction[**A, B] = Callable[A, B]
type Predicate = Callable[..., bool]

