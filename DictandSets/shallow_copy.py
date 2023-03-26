from contents import recipes 
import copy




def copy_animals(d: dict) -> dict: 
    recipes_deep_copy = {}
    
    for key, value in d.items():
        new_value = value.copy()
        recipes_deep_copy[key] = new_value
    
    return recipes_deep_copy

recipes_copy = copy_animals(recipes)
recipes_copy["Egg sandwich"]["bread"] = 400
print(recipes_copy["Egg sandwich"]["bread"])
print(recipes["Egg sandwich"]["bread"])
    
    

#things = animals.copy() # when you use shallow dot cop() it will not be update.
# animals["teddy"] = "toy"  
# things = copy.deepcopy(animals) 

# print(id(things["teddy"]),things["teddy"])
# print(id(animals["teddy"]), animals["teddy"]) 


# print()

# things["teddy"].append("toy")
# print(things["teddy"])
# print(animals["teddy"]) 

