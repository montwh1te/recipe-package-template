import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'recipe_manager')))

from recipe_manager.components.ingredients import Ingredients
from recipe_manager.components.recipe import Recipe
# from recipe_manager.metrics.nutrition import total_nutrition_food
# from recipe_manager.metrics.conversions import convertion_measures

salt = Ingredients('Salt', 200, 'g')
sugar = Ingredients('Sugar', 150, 'g')
flour = Ingredients('Flour', 300, 'g')

pancake_recipe = Recipe("Pancake", 4)
pancake_recipe.add_ingredient(salt)
pancake_recipe.add_ingredient(sugar)
pancake_recipe.add_ingredient(flour)

pancake_recipe.add_step("Mix the ingredients.", 1)
pancake_recipe.add_step("Cook on a hot pan.", 2)

print(pancake_recipe)
