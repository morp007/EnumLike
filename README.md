Another enum for python (tested on Python 2.7.15, with PyCharm (linter)).

Quickstart:
```python
from enum_like import EnumLike, Args


class A(EnumLike):
    pass


Args.VAR_1 = A(1)


def f(a):
    """
    Args:
        a(A)

    """
    print '{}'.format(a)


if __name__ == '__main__':
    f(Args.VAR_1)
```

Usage:
See extended example in main.py 
