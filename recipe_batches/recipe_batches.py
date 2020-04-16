#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  batch_counter = 0
  while True:
    if len(recipe) != len(ingredients):
      return batch_counter
    elif len(recipe) and len(ingredients) == 1:
      for i in ingredients:
        if recipe[i] > ingredients[i]:
          return batch_counter
        else: 
          ingredients[i] = ingredients[i] - recipe[i]
          batch_counter = batch_counter + 1 
    else:
      for i in ingredients:
        if recipe[i] > ingredients[i]:
          batch_counter = batch_counter // len(ingredients)
          return batch_counter
        else: 
          ingredients[i] = ingredients[i] - recipe[i]
          batch_counter = batch_counter + 1 
          
#if 

print(recipe_batches({ 'milk': 2, 'sugar': 40, 'butter': 20 }, { 'milk': 5, 'sugar': 120, 'butter': 500 }))
if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))