from Recipe import VegetarianRecipe, DessertRecipe
from User import User
from Rating import Rating

if __name__ == "__main__":
    vegetarian_recipe = VegetarianRecipe(
        "Vegetable Stir-Fry",
        ["Broccoli", "Carrots", "Bell Peppers", "Soy Sauce"],
        ["1. Cut the vegetables into small pieces.",
         "2. Heat the oil in a pan and stir-fry the vegetables.",
         "3. Add soy sauce for flavor."]
    )

    dessert_recipe = DessertRecipe(
        "Chocolate Brownies",
        ["Flour", "Sugar", "Cocoa Powder", "Eggs"],
        ["1. Mix the dry ingredients.",
         "2. Add eggs and stir until smooth.",
         "3. Bake in a preheated oven."]
    )

    user1 = User("Alice", "alice@examplegmail.com")
    user2 = User("Bob", "bob@examplegmail.com")

    user1.add_favorite_recipe(vegetarian_recipe)
    user2.add_favorite_recipe(dessert_recipe)

    rating1 = Rating(vegetarian_recipe, user1, 4.5)
    rating2 = Rating(dessert_recipe, user2, 5.0)

    print("Alice's favorite recipes:")
    for recipe in user1.favorite_recipes:
        recipe.display_recipe()

    print("Bob's favorite recipes:")
    for recipe in user2.favorite_recipes:
        recipe.display_recipe()


