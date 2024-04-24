class Recipe:

    all_recipes = []

    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients

    def disp_recipe(self):
        print(f"Recipe: {self.name}")
        print("Ingredients")
        for ing in self.ingredients:
            print(f"- {ing}")

    @classmethod
    def disp_all_recipes(cls):
        print("All Recipes")
        for recipe in cls.all_recipes:
            print(recipe.name)

    @staticmethod
    def convert_to_g(amount, unit):
        if unit == "spoons":
            return amount * 20
        elif unit == "cups":
            return amount * 236


# Create instances of Recipe
omelette_du_fromage = Recipe("Omelette", ["eggs", "cheese", "veggies"])
omelette_du_fromage.disp_recipe()

serge_style_omelette = Recipe("Ommu", ["eggs", "flavour", "love"])
serge_style_omelette.disp_recipe()

# Add instances to the list of all recipes
Recipe.all_recipes.append(omelette_du_fromage)
Recipe.all_recipes.append(serge_style_omelette)

# Display recipe details
Recipe.disp_all_recipes()

# Static method example
cups = Recipe.convert_to_g(2, "cups")
print(f"2 cups in grams is {cups} grams")
