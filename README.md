Some stuff for arguments and their typos.

Contains:
* Base type (class name: EnumLike)
* Args owner (class name: Args)

Main ideas:
1. wrap some values with type
1. (сравнивать по указателю, а не содержимому)

Quickstart:
```python
from enum_like import EnumLike, Args


# add some type
class A(EnumLike):
    pass


# add some variable, that hold some value
Args.VAR_1 = A(1)


# function with docstring that uses our type
def f(a):
    """
    Args:
        a(A)

    """
    print '{}'.format(a)


if __name__ == '__main__':
    # just function call
    f(a=Args.VAR_1)
```

See extended example in main.py

Tested with Python 2.7.15, PyCharm (linter).
