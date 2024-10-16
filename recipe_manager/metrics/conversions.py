from unitconvert import mass, volume

def convertion_measures(ingredient_name, quantity, from_unit, to_unit):
    
    print(f"Converting {quantity} {from_unit} of {ingredient_name} to {to_unit}:")
    
    if from_unit == 'cup' and to_unit == 'milliliters':
        result = volume.cups_to_milliliters(quantity)
    elif from_unit == 'grams' and to_unit == 'ounces':
        result = mass.grams_to_ounces(quantity)
    elif from_unit == 'milliliters' and to_unit == 'teaspoons':
        result = volume.milliliters_to_teaspoons(quantity)
    elif from_unit == 'teaspoons' and to_unit == 'milliliters':
        result = volume.teaspoons_to_milliliters(quantity)
    elif from_unit == 'ounces' and to_unit == 'grams':
        result = mass.ounces_to_grams(quantity)
    elif from_unit == 'milliliters' and to_unit == 'cups':
        result = volume.milliliters_to_cups(quantity)
    elif from_unit == 'grams' and to_unit == 'kilograms':
        result = mass.grams_to_kilograms(quantity)
    elif from_unit == 'kilograms' and to_unit == 'grams':
        result = mass.kilograms_to_grams(quantity)
    else:
        result = "Conversão não suportada"
        
    print(f'This value could be converted. The result is {result}{to_unit} of {ingredient_name}')
