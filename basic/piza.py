#Arbitrary number of arguments
def make_Piza(size, *ingredients):
    strIngredients = ', '.join(ingredients)    
    print(f"A {size} inches PIZA with {strIngredients}")
    
# make_Piza(6, "Chicken", "Tomato", "Mushroom", "Onion", "Garlic")


#Using arbitrary keyword arguments
def make_Inventor(name, **prams):
    prams["Inventor"] = name
    print(prams)
    
# make_Inventor("Saurav", Country = 'Bangladesh', Price = 550, Description = "Special for vegeterians")

    