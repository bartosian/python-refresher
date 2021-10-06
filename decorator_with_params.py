import time

DEFAULT_FMT = "[{elapsed:0.8f}s] {name}({args}) -> {result}"

registry = set()


def register(active=True):
    def decorate(func):
        print("running register" f"(active={active}) -> decorate({func})")

        if active:
            registry.add(func)
        else:
            registry.discard(func)

        return func

    return decorate


@register(active=False)
def f1():
    print("running f1()")


@register()
def f2():
    print("running f2()")


def f3():
    print("running f3()")


def clock(fmt=DEFAULT_FMT):
    def decorate(func):
        def clocked(*_args):
            pass

        return clocked

    return decorate


if __name__ == "__main__":

    @clock()
    def snooze(seconds):
        time.sleep(seconds)

    for i in range(3):
        snooze(0.123)
