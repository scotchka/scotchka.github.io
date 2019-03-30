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

