from liskov import Vegetable, Meat


class Vegetarian:
    def eat(self, food):
        if not isinstance(food, Vegetable):
            return super().eat(food)
        print(food.name, "YUM!")


class Carnivore:
    def eat(self, food):
        if not isinstance(food, Meat):
            return super().eat(food)
        print(food.name, "YUM!")


class Omnivore(Vegetarian, Carnivore):
    pass
