#import math for math.ceil()

import math

#create dictionary of recipe ingredients

recipe_dict = {
               'eggs':{'amount':2.0,'measure':'','price':.22,'oz': 0,'state':''},
               'milk':{'amount': 1.0,'measure':'cups','price':.12,'oz': 8,'state':'lqd'},
               'butter':{'amount': .5,'measure':'cups','price':2.95,'oz': 8,'state':'dry'},
               'white sugar':{'amount': 1,'measure':'cups','price':.35,'oz': 8,'state':'dry'},
               'vanilla extract':{'amount': 1.0,'measure':'tsp','price':.41,'oz':0.166667,'state':'lqd'},
               'unsweetened cocoa powder':{'amount': .33,'measure':'cups','price':5.24,'oz': 8,'state':'dry'},
               'flour':{'amount': .5,'measure':'cups','price':.74,'oz': 8,'state':'dry'},
               'salt':{'amount': .25,'measure':'tsp','price':.01,'oz':0.166667,'state':'dry'},
               'baking powder':{'amount': .25,'measure':'tsp','price':.06,'oz':0.166667,'state':'dry'}
               }
recipe_yield = 16

#to convert to larger measures
cup_oz = 8
tsp_oz = .166667
gal_oz = 128
#to convert measure oz to weight oz
lb_oz_flour = 26.64
lb_oz_sugar = 18

#header

print("*" * 32 + "\n" + "* The Best Brownie Recipe Ever *\n" + "*" * 8 + "Revious/Gresham" + "*" * 9 + "\n")


#1 check input for valid, positive integer

while True:
    try:
        units_required = int(input("Please enter desired number of brownies (2in x 2in): "))
        if units_required < 0:
            print("Please input a positive integer...Try again")
            continue
        break
    except ValueError:
        print ("That was not a valid number. Please try again...")


#2 create total_cost list to track totals through loop/create recipe_details list to capture ampunts and measures to update instructions

total_cost = []
recipe_details = []

print("Ingredients:")
print("-" *30)


#4 Iterate through dictionary items to calculate amounts relative to request, desired measurement units, and implement correct formatting

for item in recipe_dict.items():
    
    total_oz = (item[1]['amount']/recipe_yield) * (item[1]['oz'] * units_required)
    conv_amount = (item[1]['amount']/recipe_yield) * units_required
    cost = conv_amount * item[1]['price']
    cost_format = format(cost,'.2f')

#5 check each measures in oz to convert to easy to use units(convert dry volume measures to weight measure--lbs,etc and liquid tsp and cups to gallons as required,etc)

    if item[1]['measure']=='':
        mm = ''
        ma = math.ceil(conv_amount)
    elif total_oz < 2:
        mm = "tsp"
        ma = format(total_oz/tsp_oz,'.2f')
    elif total_oz <= 16:
        mm = "cups"
        ma = format(total_oz/cup_oz,'.2f')
    elif total_oz <= 32:
        if item[1]['state']=='lqd':
            mm = "cups"
            ma = format(total_oz/cup_oz,'.2f')
        else:
            if item[0] == 'flour' or item[0] == 'unsweetened cocoa powder':
                mm = "lbs"
                ma = format(total_oz/lb_oz_flour,'.2f')
            else:
                mm = "lbs"
                ma = format(total_oz/lb_oz_sugar,'.2f')
    else:
        if item[1]['state']=='lqd':
            mm = "gallons"
            ma = format(total_oz/gal_oz,'.2f')
        else:
            if item[0] == 'flour' or item[0] == 'unsweetened cocoa powder':
                mm = "lbs"
                ma = format(total_oz/lb_oz_flour,'.2f')
            else:
                mm = "lbs"
                ma = format(total_oz/lb_oz_sugar,'.2f')
#6 print ingredient line
    print(ma,mm ,item[0],"at a cost of $",cost_format)
#7 create list to update recipe instructions   
    
    recipe_details.append(str(ma) + " " + str(mm))

#8 append array with costs

    total_cost.append(cost)

#9 adjust recipe directions to reflect variable amounts and units of measure

recipe_time = ("Preparation time = 25 minutes \nCooking time = 35 minutes")
recipe_instructions = (
                        "Steps:\n" + 
                        "1. Preheat the oven to 350 degrees.\n" + 
                        "2. Grease and flour {} 8inch baking dish(es).\n".format(round(units_required/recipe_yield)) + 
                        "3. In a large saucepan, melt {} butter.\n".format(recipe_details[2]) +
                        "4. Remove from heat, and stir in sugar, eggs, and {} vanilla.\n".format(recipe_details[4]) +
                        "5. Beat in {} cocoa, {} flour, salt, and baking powder.\n".format(recipe_details[5],recipe_details[6]) +
                        "6. Spread batter into prepared pan(s).\n" + 
                        "7. Bake in preheated oven for 25 to 30 minutes. Do not overcook.\n"+ 
                        "8. Serve warm and enjoy!"
                      )    
#10 Print total yield, instructions and total cost for ingredients
  
print("-" *30)
print("Total Cost for",units_required," 2in x 2in Brownies: $",format(sum(total_cost),'.2f'))
print("*" * 32)
print("Directions:")
print("-" * 32)
print(recipe_time)
print("-" * 32)
print(recipe_instructions)
print("*" * 32)
