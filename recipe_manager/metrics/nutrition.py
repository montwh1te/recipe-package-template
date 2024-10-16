import noms

client = noms.Client("xfUZN1ZzQ46fKCIrOmCwUqeIVrXPlcyyoGW2S4HD")

def total_nutrition_food(recipe_obj_name):
    food_list = []
    for ingredient in recipe_obj_name.ingredients:
        search_results = client.search_query(ingredient.name)
        if search_results and search_results.ingredients:
            food_item = {
                'food_id': search_results.ingredients.id,
                'quantity': ingredient.quantity,
            }
            food_list.append(food_item)
    nutrition_recipe = noms.Meal(food_list)
    print('@@@@@@@ Medidas da Receita @@@@@@@')
    print(nutrition_recipe[['name', 'value', 'unit']])
