from typing import Callable
from .typedefs import *

def compose[**A, **B, C](
        f: ParametricFunction[B, C], 
        g: ParametricFunction[A, B]
    ) -> ParametricFunction[A, C]:
    
    def h(*args: A.args, **kwargs: A.kwargs) -> C:
        if args or kwargs:
            return f(g(*args, **kwargs))
        return f(g())

    return h


def flip[A, B, C](f: Callable[[A, B], C]) -> Callable[[B, A], C]:
    def flipped(b: B, a: A) -> C:
        return f(a, b)
    return flipped 


def identity[A](x: A) -> A:
    return x

def const[A, B](a: A, b: B) -> A:
    return a

def join[A, B](f: Callable[[A, A], B]) -> Callable[[A], B]:
    def inner(a: A) -> B:
        return f(a, a)
    return inner

def s[A, B, C](f: Callable[[A, B], C], g: Callable[[A], B]) -> C:
    def inner(x: A) -> C:
        return f(x, g(x))
    return inner



__all__ = [
    "compose", 
    "flip", 
    "identity", 
    "join", 
    "s"
]


