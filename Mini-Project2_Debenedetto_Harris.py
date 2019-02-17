
print ('Harris & Debenedetto Beignets Recipe :)' "\n")


Beignets =int(input("How many beignets would you like to make?"))
Yeast=1.00* ((Beignets*1.0)/36)
Milk=0.50 * ((Beignets*1.0)/36)
Water=0.75 * ((Beignets*1.0)/36)
Sugar=0.25 * ((Beignets*1.0)/36)
Egg=1.00 * ((Beignets*1.0)/36)
Flour=3.50 * ((Beignets*1.0)/36)
Butter=2.00 * ((Beignets*1.0)/36)
print("%.2f"%Yeast, "teaspoons of Yeast")
print("%.2f"%Milk,"cups of milk")
print("%.2f"%Water,"cups of water")
print("%.2f"%Sugar,"cups of sugar")
print("%.2f"%Egg,"eggs")
print("%.2f"%Flour,"cups of flour")
print("%.2f"%Butter,"tablespoons of Butter \n")



Item1 = 0.5
Item2 = 1.50
Item3 = .75
Item4 = 1.50
Item5 = .25
Item6 = .60
Item7 = .25

if Beignets >= 300 and Beignets < 600:
    Item1 = Item1 * .80
    Item2 = Item2 * .80
    Item3 = Item3 * .80
    Item4 = Item4 * .80
    Item5 = Item5 * .80
    Item6 = Item6 * .80
    Item7 = Item7 * .80

elif Beignets >= 600:
    Item1 = Item1 * .70
    Item2 = Item2 * .70
    Item3 = Item3 * .70
    Item4 = Item4 * .70
    Item5 = Item5 * .70
    Item6 = Item6 * .70
    Item7 = Item7 * .70

    
print ('Price of yeast is: $', "%.2f"%Item1, ' per teaspoon.')
print ('Price of milk is: $', "%.2f"%Item2, ' per cup of milk.') 
print ('Price of water is: $', "%.2f"%Item3, ' per cup of water.')
print ('Price of sugar is: $', "%.2f"%Item4, ' per cup of sugar.')
print ('Price of eggs is: $', "%.2f"%Item5, ' per egg.')
print ('Price of flour is: $', "%.2f"%Item6, ' per cup of flour.')
print ('Price of butter is: $', "%.2f"%Item7, ' per tablespoon of butter.\n')    
 
#calculate the total of 7 items

TotalCost=((Item1 * Yeast) + (Item2 * Milk) + (Item3 * Water) + (Item4 * Sugar) + (Item5 * Egg) + (Item6 * Flour)  + (Item7 * Butter))

print ('Cost of yeast needed for', Beignets, 'beignets is: $', "%.2f"%(Item1 * Yeast))
print ('Cost of milk needed for', Beignets, 'beignets is: $', "%.2f"%(Item2 * Milk))
print ('Cost of water needed for', Beignets, 'beignets is: $', "%.2f"%(Item3 * Water))
print ('Cost of sugar needed for', Beignets, 'beignets is: $', "%.2f"%(Item4 * Sugar))
print ('Cost of eggs needed for', Beignets, 'beignets is: $', "%.2f"%(Item5 * Egg))
print ('Cost of flour needed for', Beignets, 'beignets is: $', "%.2f"%(Item6 * Flour))
print ('Cost of butter needed for', Beignets, 'beignets is: $', "%.2f"%(Item7 * Butter), '\n')
print ('The total cost for ingredients will be: $', "%.2f"%TotalCost,'\n')

print ('Recipe: \n')
print ('Recipe creates 36 Beignets')
print ('Prep time is 20 minutes')
print ('Cook time is 20 minutes')
print ('Inactive time is 2 hours')
print ('Total Time is 2 hours and 40 minutes \n')
print ('Ingredients:')
print ('3/4 cups of water')
print ('1/4 cup of sugar')
print ('1 teaspoon of yeast')
print ('1 large egg')
print ('3 1/2 cups of flour')
print ('1/2 cups of milk')
print ('2 tablespoons of butter \n')
print ('Directions:')
print ('In the bowl of a stand mixer fitted with the dough hook combine the water, sugar, yeast, egg, evaporated milk, and half the flour. Mix until combined. With the mixer on low speed, add the butter and then the remaining flour and salt and increase the speed to medium. Knead until the dough is smooth and just tacky.\n')
print ('Place the dough in an oiled bowl and cover with plastic wrap. Let rise in a warm place for about 2 hours. Do not skimp on the rising time! To make ahead: store the dough in the fridge for up to 4 days. Let come to room temperature before using.\n')
print ('Preheat oil in a deep-fryer to 360°F. Place the confectioners’ sugar in a large bowl.\n')
print ('Roll the dough out to about 1/4-inch thickness and cut into squares. Deep-fry, flipping constantly, until they become a golden color on both sides, about 3 to 4 minutes total. The beignets should float to the surface very quickly after being added to the oil. If they do not, they oil is not hot enough.\n')       
print ('After beignets are fried, drain them for a few seconds on paper towels. Keep the freshly fried beignets warm in a 200° oven up to 30 minutes. Toss them into the bowl of confectioners sugar while still hot.\n')       
