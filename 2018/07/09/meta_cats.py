class Cat:
    def __repr__(self):
        return "<🐱>"


class MetaCat(type):
    def __repr__(cls):
        return "<class 🐱>"


class FancyCat(metaclass=MetaCat):
    pass
