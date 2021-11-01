consonants = {}.fromkeys("bcdfghjklmnpqrstvwzy", "consonant")
for k, v in consonants.items():
   print(k, v)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}
popped = fast_food_items.pop("McDonald's")
print(popped)

popped_items = fast_food_items.popitem()
print(fast_food_items)