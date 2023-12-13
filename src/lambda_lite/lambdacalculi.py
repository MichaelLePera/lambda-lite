from typing import TypeVar
from typing import ParamSpec
from typing import Iterator

from functools import partial


_A = TypeVar("_A")
_B = TypeVar("_B")
_C = TypeVar("_C")
_D = TypeVar("_D")
_P = ParamSpec("_P")


class Lambda:

    def __init__(self, abstraction: str) -> None:
        self.__params, self.__application = abstraction.split(".")

    def _iterargs(self, arguments: dict, offset: int, it: Iterator[str]):
        for i, step in enumerate(it):
            if step == "(":
                offset, value = self._execute(
                    arguments, i + offset, it
                )
                offset -= i

            elif step == ")":
                break
            else:
                value = arguments[step]
            yield i + offset, value

    def _execute(self, arguments: dict, offset: int, it: Iterator[str]):
        result = None
        i = offset
        for idx, step in self._iterargs(arguments, offset, it):
            i = idx
            if i == offset:
                result = step
            else:
                if not callable(result):
                    raise TypeError(f"{result} is not callable.")
                result = partial(result, step)
        return i, result()

    def __call__(self, *args: _P.args, **kwargs: _P.kwargs):
        if (len(args) + len(kwargs)) != len(self.__params):
            raise AttributeError("Too many/little arguments.")
        arguments = kwargs
        i = 0
        for v in args:
            while self.__params[i] in arguments:
                i += 1
            arguments[self.__params[i]] = v

        _, result = self._execute(arguments, 0, iter(self.__application))
        return result

    def __str__(self) -> str:
        return self.__params + "." + self.__application


if __name__ == "__main__":
    import operator
    b = Lambda("abc.a(bc)")

    def increment(x: int) -> int:
        return x + 1

    def isEven(x: int) -> bool:
        return x % 2 == 0
    print(b)
    print(">", b(isEven, increment, 1), "= True")
    print(">", b(isEven, increment, 6), "= False")
    s = Lambda("abc.ac(bc)")
    print(s)
    print(">", s(operator.eq, increment, 1), "= False")
    b1 = Lambda("abcd.a(bcd)")
    print(b1)
    print(">", b1(isEven, operator.mul, 1, 2), "= True")
    print(">", b1(isEven, operator.mul, 3, 7), "= False")

