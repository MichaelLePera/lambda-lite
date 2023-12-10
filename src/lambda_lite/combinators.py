from typing import Callable

from .typedefs import *


def compose[**A, **B, C](f: ParametricFunction[B, C], g: ParametricFunction[A, B]) -> ParametricFunction[A, C]:
    def h(*args: A.args, **kwargs: A.kwargs) -> C:
        if args or kwargs:
            return f(g(*args, **kwargs))
        return f(g())

    return h


def flip_[A, B, C](f: Callable[[A, B], C]) -> Callable[[B, A], C]:
    def flipped(b: B, a: A) -> C:
        return f(a, b)

    return flipped


def id_[A](x: A) -> A:
    """Identity combinator.

    λa.a

    """
    return x


def const_[A, B](a: A, b: B) -> A:
    """K combinator.

    λab.a

    """
    return a


def join_[A, B](f: Callable[[A, A], B]) -> Callable[[A], B]:
    def inner(a: A) -> B:
        return f(a, a)

    return inner


def s[A, B, C](f: Callable[[A, B], C], g: Callable[[A], B]) -> C:
    def inner(x: A) -> C:
        return f(x, g(x))

    return inner


def on_[A, B, C](f: Callable[[B, B], C], g: Callable[[A], B], a: A, b: A) -> C:
    """psi combinator"""
    return f(g(a), g(b))


def applicator[A, B](f: Callable[[A], B], a: A) -> B:
    """i-star combinator"""
    return f(a)


def becard_[
    A, B, C, D
](f: Callable[[C], D], g: Callable[[B], C], h: Callable[[A], B], a: A) -> D:
    """B3 combinator"""
    return f(g(h(a)))


def blackbird_[
    A, B, C, D
](f: Callable[[C], D], g: Callable[[A, B], C], a: A, b: B) -> D:
    return f(g(a, b))


__all__ = ["compose", "flip_", "id_", "join_", "s"]
