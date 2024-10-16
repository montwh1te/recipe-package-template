from recipe_manager.components.ingredients import Ingredients

class Recipe:
    def __init__(self, name, servings):
        self.name = name
        self.servings = servings
        self.ingredients = []
        self.steps = []
        
    def __str__(self):
        return f'''
@@@@@@@ Recipe Details @@@@@@@

Name: {self.name}
Servings Amount: {self.servings}
{self.list_ingredients()}
{self.list_steps()}'''

    def add_step(self, step_message, step_num):
        self.steps.insert((step_num-1), step_message)
        
    def edit_step(self, step_num, step_message):
        if 0 <= (step_num-1) < (len(self.steps)):
            self.steps[step_num-1] = step_message
    
    def del_step(self, step_num):
        self.steps = [step for step in self.steps if (step_num-1) != self.steps.index(step)]
        
    def list_steps(self):
        return f'''
@@@@@@@ Steps Order @@@@@@@ 
    
{f"".join([f"{enum + 1}. {step}\n" for enum, step in enumerate(self.steps)])}'''
        
    def adjust_servings(self, new_servings):
        factor_num = new_servings / self.servings
        for ingredient in self.ingredients:
            ingredient.quantity *= factor_num
        self.servings = new_servings
        
    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)
        
    def edit_ingredient(self, ingredient_name, ingredient_quantity=None, ingredient_unit=None):
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                if ingredient_quantity:
                    ingredient.quantity = ingredient_quantity
                elif ingredient_unit:
                    ingredient.unit = ingredient_unit
                    
    def remove_ingredient(self, ingredient_name):
        self.ingredients = [ingredient for ingredient in self.ingredients if ingredient.name != ingredient_name]
    
    def check_ingredient(self, ingredient_name):
        for ingredient in self.ingredients:
            if ingredient.name == ingredient_name:
                self.list_ingredients()
                return True
        print('Ingredient not found :/')
            
    def list_ingredients(self):
       return f'''
@@@@@@@ Ingredients List @@@@@@@ 
    
{"\n".join(str(ingredient) for ingredient in self.ingredients)}'''