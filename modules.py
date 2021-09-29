import builtins

print(__name__)

import importlib

importlib.reload(builtins)

_abs = builtins.abs


def abs(str_or_num):
    if isinstance(str_or_num, str):
        return "".join(sorted(set(str_or_num)))

    return _abs(str_or_num)


builtins.abs = abs

TEST = "b"
