#Chocolate Chip Cookies recipe done by Ashley Zamora Nora Gonzalez


cookies=input("Enter number of cookies needed:\n")
a=(int(cookies))
brown_sugar=(a/24)*1

            
b_sugar_price=(a/24)*4

butter=(a/24)*1
but_price=(a/24)*2

white_sugar=(a/24)*1
w_sugar_price=(a/24)*5.42

chocolate=(a/24)*2
c_price=(a/24)*5.98

baking_soda=(a/24)*.5
bs_price=(a/24)*2.27

baking_powder=(a/24)*1
bp_price=(a/24)*4.40

eggs=(a/24)*2
eg_price=(a/24)*2.33

v_extract=(a/24)*2
v_price=(a/24)*6.92

m_flour=(a/24)*6
mf_price=(a/24)*10.98

all_flour=(a/24)*3
af_price=(a/24)*3.47

sea_salt=(a/24)*2
ss_price=(a/24)*5.88

table_salt=(a/24)*2.75
t_salt_price=(a/24)*3.98


flour=input("\nWhat type of flour do you intend to use: all purpose or almond?\n")

if flour =="all purpose":
    print(" For all purpose flour, you will need "+'%.2f' % all_flour+" cups of flour for recipe. Costing approximately:"+"$" +'%.2f' % af_price)
elif flour=="all":
    print(" For all purpose flour, you will need "+'%.2f' % all_flour+" cups of flour for recipe. Costing approximately:"+"$" +'%.2f' % af_price)
elif flour=="all purpose flour":
    print(" For all purpose flour, you will need "+'%.2f' % all_flour+" cups of flour for recipe. Costing approximately:"+"$" +'%.2f' % af_price)
elif flour=="almond":
    print(" For almond flour, you will need "+'%.2f' % m_flour+" cups of flour for recipe. Costing approximately:"+"$" +'%.2f' % mf_price)
elif flour=="almond flour":
    print(" For almond flour, you will need "+'%.2f' % m_flour+" cups of flour for recipe. Costing approximately:"+"$" +'%.2f' % mf_price)
    
#m_flour=almond
#all_flour=all purpose

salt=input("\nWhat type of salt would you like to use table or sea?\n")

if salt=="sea":
    print(" For sea salt, you will need "+'%.2f' % sea_salt+"tsp of salt for recipe. Costing approximately:"+"$"+ '%.2f' % ss_price)
elif salt=="sea salt":
    print(" For sea salt, you will need "+'%.2f' % sea_salt+"tsp of salt for recipe. Costing approximately:"+"$"+ '%.2f' % ss_price)
elif salt=="table":
    print(" For table salt, you will need "+'%.2f' % table_salt+"tsp of salt for recipe. Costing approximately:"+"$"+ '%.2f' % t_salt_price)
elif salt=="table salt":
    print(" For table salt, you will need "+'%.2f' % table_salt+"tsp of salt for recipe. Costing approximately:"+"$"+ '%.2f' % t_salt_price)

#total price possibilities based of input------

total_price_allflour_option=(b_sugar_price+but_price+w_sugar_price+c_price+bs_price+bp_price+eg_price+v_price+af_price+ss_price)# if choosing all purpose flour *w/sea salt
total_price_allflour_option_tsalt=(b_sugar_price+but_price+w_sugar_price+c_price+bs_price+bp_price+eg_price+v_price+af_price+t_salt_price)#if choosing all purpose flour *w/table salt
total_price_almond_option=(b_sugar_price+but_price+w_sugar_price+c_price+bs_price+bp_price+eg_price+v_price+mf_price+ss_price)#if choosing almond flour *w/sea salt
total_price_almond_option_tsalt=(b_sugar_price+but_price+w_sugar_price+c_price+bs_price+bp_price+eg_price+v_price+mf_price+t_salt_price)#if option if choosing almond flour *w/tablesalt

#printed ingredients with prices-----(
print("\n You will need the rest of the following ingredients for your cookies:")
print('%.2f' % brown_sugar+" cups of brown sugar costing about:"+"$"+'%.2f' % b_sugar_price)

print('%.2f' % butter+" cups of softened butter costing about:"+"$"+'%.2f' % but_price)
print('%.2f' % white_sugar+" cups of sugar costing about:"+"$"+'%.2f' % w_sugar_price)
print('%.2f' % chocolate+" cups of chocolate chips costing about:"+"$"+'%.2f' % c_price)
print('%.2f' % baking_soda+" tsp of baking soda costing about:"+"$"+'%.2f' % bs_price)
print('%.2f' % baking_powder+" tsp of baking powder costing about:"+"$"+'%.2f' % bp_price)
print(int(round(eggs))," large eggs costing about:","$"+'%.2f' % eg_price)
print('%.2f' % v_extract+" tsp vanilla extract costing about:"+"$"+'%.2f' % v_price)

#------------the following are totals if they enter any form of all purpose+sea salt
if (flour=="all purpose"
    and salt=="sea"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option)
elif (flour=="all purpose"
    and salt=="sea salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option)

elif (flour=="all"
      and salt=="sea"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option)
elif (flour=="all"
      and salt=="sea salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option)
        
elif (flour=="all purpose flour"
      and salt=="sea"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option)
elif (flour=="all purpose flour"
      and salt=="sea salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option)

#--------the folowing are totals if they enter any form of almond+sea salt
elif (flour=="almond"
      and salt=="sea"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option)
elif (flour=="almond flour"
      and salt=="sea"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option)

elif (flour=="almond"
      and salt=="sea salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option)
elif (flour=="almond flour"
      and salt=="sea salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option)

#--------the following are totals if they enter any form of all purpose+table salt
elif (flour=="all purpose"
      and salt=="table"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option_tsalt)
elif (flour=="all"
      and salt=="table"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option_tsalt)
elif (flour=="all purpose flour"
      and salt=="table"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option_tsalt)
elif (flour=="all purpose"
      and salt=="table salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option_tsalt)
elif (flour=="all"
      and salt=="table salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option_tsalt)
elif (flour=="all purpose flour"
      and salt=="table salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_allflour_option_tsalt)

#-----the following are totals if they enter any form of almond+table salt
elif (flour=="almond"
      and salt=="table"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option_tsalt)
elif (flour=="almond flour"
      and salt=="table"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option_tsalt)
elif (flour=="almond"
      and salt=="table salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option_tsalt)
elif (flour=="almond flour"
      and salt=="table salt"):
        print("\n Total price of cookies: $",'%.2f' % total_price_almond_option_tsalt)




        
print("\n")
#Cookie Recipe-----
print("***************************************************************")
print(" Recipe for Ashley & Nora's Best Cookies Ever!\n")
print("1. Preheat oven to 375 degrees Fahrenheit. Line baking pan with parchment paper and set aside\n")
print("2. In seperate bowl mix flour, baking soda, salt, baking powder. Set aside.\n")
print("3. Cream together butter and sugars until combined.\n")
print("4. Beat in eggs and vanilla until fluffy.\n")
print("5. Mix in the dry ingredients until combined.\n")
print("6. Add chocolate chips and mix well.\n")
print("7. Roll dough into small balls and place them evenly spaced on your prepared cookie sheets.\n")
print("8. Bake in preheated oven for approximately 8-10 minutes. Take out when they are just BARELY starting to turn brown.\n")
print("Let them sit on the baking pan for 2 minutes before removing to cooling rack.\n")
print("\n")
print("Enjoy!!!")
print("***************************************************************")




