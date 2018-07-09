class Cat:
    def __repr__(self):
        return "<😻>"


class MetaCat(type):
    def __repr__(cls):
        return cls.repr_string


class FancyCat(metaclass=MetaCat):
    repr_string = "<class 😻>"

