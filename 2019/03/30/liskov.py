class Food:
    def __init__(self, name, calories):
        self.name = name
        self.calories = calories


class Vegetable(Food):
    is_leafy = True


class Meat(Food):
    is_bloody = True


def get_calories(food):
    return food.calories


class Omnivore:
    def eat(self, food):
        print(food.name, "YUM!")


class Vegetarian(Omnivore):
    def eat(self, food):
        if not isinstance(food, Vegetable):
            raise Exception(food.name + " EWW")
        super().eat(food)


class Carnivore(Omnivore):
    def eat(self, food):
        if not isinstance(food, Meat):
            raise Exception(food.name + " EWW")
        super().eat(food)
