#ceviche.py, by Glenn Cianci and Andre Teran, 3-2-2019
#ver 1.2
#This program asks for the amount of ceviche portions and if the user wants it spicy,then displays the total cost,  total ingredients, recipe, nutrition info for 1 serving and the user's choice of spicy/not spicy.)


#1.0 Quantity Input
#Requests input of number of servings and determines how many units of 4 will be produced.
quantityInput = int ( input ('Welcome to CevicheBot 1.2' + (u'\u00AE')+ '\nHow many portions of Ceviche do you want? '))

import math
recipeUnits = math.floor(quantityInput / 4)
recipeRemainder = quantityInput % 4
zeroZero = 0

if recipeRemainder > zeroZero:
	recipeUnits = recipeUnits + 1

#2.0 Spicy Input
#Requests input of "y", "Y", "n", or "N" if the user wants the food spicy or not.

spicyTest_y = 'y'
spicyTest_Y = 'Y'
spicyTest_yes = 'yes'

spicyInput = input ('Do you want it spicy? (y/n)')
if spicyInput == spicyTest_y or spicyInput == spicyTest_Y or spicyInput == spicyTest_yes:
	print('The spice must flow.')
else:
	print ('Okay cool cat.')

#3.0 Recipe Formula
# Multiplies the quantity of ingredient by the number of units.

amountShrimp = int ( 1 * int(recipeUnits) )
amountOnion = math.ceil ( 0.5 * int (recipeUnits) )
amountCucumber = int ( 1 * int (recipeUnits) )
amountTomatoes = int ( 3 * int (recipeUnits) )
amountJalapeno = int ( 1 * int (recipeUnits) )
amountCilantro = math.ceil ( 0.5 * int (recipeUnits) )
amountLime = math.ceil ( 1.25 * int (recipeUnits) )
amountLemon = math.ceil ( 0.25 * int (recipeUnits) )
amountWorcestershire = float ( 0.5 * int (recipeUnits) )
amountAvocado = int ( 1 * int (recipeUnits) )
amountTostadas = int ( 1 * int (recipeUnits) )

#4.0 Cost Formula
# Multiplies the cost of ingredients by the number of units.

costShrimp = float ( 5 * int (recipeUnits) )
costOnion = float ( 0.5 * int (recipeUnits) )
costCucumber = float ( 0.5 * int (recipeUnits) )
costTomatoes = float ( 3 * int (recipeUnits) )
costJalapeno = float ( 0.5 * int (recipeUnits) )
costCilantro = float ( 1 * int (recipeUnits) )
costLime = float ( 2.5 * int (recipeUnits) )
costLemon = float ( 0.5 * int (recipeUnits) )
costWorcestershire = float ( 3.5 * int (recipeUnits) )
costAvocado = float ( 1.28 * int (recipeUnits) )
costTostadas = float ( 2 * int (recipeUnits) )

totalCost_NoJalapeno = float ( costShrimp +
		costOnion +
		costCucumber +
		costTomatoes +
		costCilantro +
		costLime +
		costLemon +
		costWorcestershire +
		costAvocado +
		costTostadas )

#5.0 Print
#Prints the byproduct of formulas and other text.


print ( '      CevicheBot 1.2' + (u'\u00AE') + 'says:' + '\n ---------------------------------- ')

print ( 'You wanted ceviche for: ' + str(quantityInput) + ' people.')

print ( 'This recipe makes enough for: ' + str (recipeUnits * 4) + ' people.')

print ('Jumbo Shrimp (oxymoron) that gave their lives to make your dream a reality: ' + str (21 * recipeUnits * 4))

if spicyInput == spicyTest_y or spicyInput == spicyTest_Y or spicyInput == spicyTest_yes:
	print ( 'You wanted it spicy?: Yes\n\n ----------------------------------\n|Total Cost: $' + str ( float (totalCost_NoJalapeno)  +  float (costJalapeno) ) + " with Jalapenos.|" + "\n ----------------------------------")
else:
	print ( 'You wanted it spicy?: No \n Total Cost: $' + str ( float (totalCost_NoJalapeno) ) + " without Jalapenos.")

print ('\n 1. Combine raw Shrimp, lemon, and lime juice in bowl. Cover and refrigerate for at least 1 hour. Ensure Shrimp is covered completely by juice.\n 2. Dice Red Onion, Cucumber, Tomatoes, Jalapeno and Cilantro and mix in separate bowl.\n 3. Add Shrimp and chopped Avocados to vegetables.\n 4. Add Worcestershire, Salt, Pepper to taste.\n 5. Mix well and serve on Tostadas. ')

print("\n List of items", "\n -------------")
print ( str (amountShrimp) + ' lbs Shrimp $'+str(costShrimp))
print ( str (amountOnion) + ' Onion(s) $' + str(costOnion))
print ( str (amountCucumber) + ' Cucumber(s) $' + str(costCucumber))
print ( str (amountTomatoes) + ' Tomato(es) $' + str(costTomatoes))
print ( str (amountCilantro)  + ' bundle(s) Cilantro $' + str(costCilantro))
print ( str (amountLime) + ' cups Lime Juice $' + str(costLime))
print ( str (amountLemon) + ' cups Lemon Juice $' + str(costLemon))
print ( str (amountWorcestershire) + ' cups Worcestershire Sauce $'+ str(costWorcestershire))
print ( str (amountAvocado) + ' Avocado(s) $'+ str(costAvocado))
print ( str (amountTostadas) + ' bags of Tostadas $'+ str(costTostadas))

if spicyInput == spicyTest_y or spicyInput == spicyTest_Y or spicyInput == spicyTest_yes:
	print ( str (amountJalapeno) + ' Jalapeno(s) $' + str(costJalapeno)+"\n")

print (' Nutrition Facts per serving \n --------------------------- \n Amount Per Serving 125g\n  Calories 216\n  Calories from Fat 72\n  Total Fat 8g             (12%)\n  Total Carbohydrates 10g  (3%)\n  Protein 26g              (52%)\n  * Percent Daily Values are based on a 2000 calorie diet.')
