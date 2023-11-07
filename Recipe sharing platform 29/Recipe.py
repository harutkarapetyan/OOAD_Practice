from abc import ABC, abstractmethod

class Recipe(ABC):
    def __init__(self, title, ingredients, instructions):
        self.title = title
        self.ingredients = ingredients
        self.instructions = instructions

    @abstractmethod
    def display_recipe(self):
        pass

class VegetarianRecipe(Recipe):
    def __init__(self, title, ingredients, instructions):
        super().__init__(title, ingredients, instructions)

    def display_recipe(self):
        print(f"Vegetarian Recipe: {self.title}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("Instructions:")
        for step in self.instructions:
            print(f"{step}")

class DessertRecipe(Recipe):
    def __init__(self, title, ingredients, instructions):
        super().__init__(title, ingredients, instructions)

    def display_recipe(self):
        print(f"Dessert Recipe: {self.title}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print("Instructions:")
        for step in self.instructions:
            print(f"{step}")