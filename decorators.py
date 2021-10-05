registry = []


def register(func):
    print(f"running register({func})")
    registry.append(func)
    return func


@register
def f1():
    print("running f1()")


@register
def f2():
    print(f"running f2()")


def f3():
    print("running f3()")


def main():
    print("running main()")
    print("registry ->", registry)
    f1()
    f2()
    f3()


def make_averager():
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count

    return averager


import time
import functools


def clock(func):
    def clocked(*args):
        t0 = time.perf_counter()
        result = func(*args)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_str = ", ".join(repr(arg) for arg in args)

        print(f"[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}")
        return result

    return clocked


def wrapped_clock(func):
    @functools.wraps(func)
    def clocked(*args, **kwargs):
        t0 = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - t0
        name = func.__name__
        arg_lst = [repr(arg) for arg in args]
        arg_lst.extend(f"{k}={v!r}" for k, v in kwargs.items())
        arg_str = ", ".join(arg_lst)

        print(f"[{elapsed:0.8f}s] {name}({arg_str}) -> {result!r}")
        return result

    return clocked


@functools.cache
@wrapped_clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


@functools.lru_cache(maxsize=2 ** 10, typed=True)
@wrapped_clock
def fibonacci_2(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == "__main__":
    fibonacci(30)
