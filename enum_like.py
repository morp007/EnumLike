class EnumLike(object):
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return str(self.value)

    def __hash__(self):
        # https://stackoverflow.com/a/7152796
        return hash(repr(self))

    def __eq__(self, other):
        # return False if self.__class__ != other.__class__ else self.value == other.value
        return id(self) == id(other)


class Args:
    _BASE_TYPE = EnumLike

    @classmethod
    def get(cls, value, class_name=None):
        """
        Args:
            value      The value
            class_name  The class name

        Returns:
            list:

        """
        if class_name is None:
            class_name = cls._BASE_TYPE

        res = list()

        for _ in dir(cls):
            if not callable(_):
                attr = getattr(cls, _)
                if isinstance(attr, class_name):
                    if attr.value == value:
                        res.append(attr)

        if not res:
            raise Exception('item not found')

        return res

    def __init__(self):
        pass
