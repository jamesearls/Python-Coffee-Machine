# Write your code here
water = int(input('Write how many ml of water the coffee machine has: '))
coffee = int(input('Write how many ml of milk the coffee machine has: '))
beans = int(input('Write how many grams of coffee beans the coffee machine has: '))
need = int(input('Write how many cups of coffee you will need: '))

water = water / 200
coffee = coffee / 50
beans = beans / 15

ans = int(min(water, coffee, beans))

if ans == need:
    print("Yes, I can make that amount of coffee")
elif ans > need:
    print("Yes, I can make that amount of coffee (and even ", ans - 1, " more than that)")
else:
    print("No, I can make only ", ans, " cups of coffee")

# drinks = int(input("Write how many cups of coffee you will need: "))
# water = drinks * 200 # 200ml per drink
# milk = drinks * 50 # 50ml per drink
# beans = drinks * 15 # 15g per drink
#
# print("For " + str(drinks) + " cups  of coffee you will need:\n"
#                         + str(water) + " ml of water\n"
#                         + str(milk) + " ml of milk\n"
#                         + str(beans) + " g of coffee beans")

# print("Starting to make a coffee\n"
#       "Grinding coffee beans\n"
#       "Boiling water\n"
#       "Mixing boiled water with crushed coffee beans\n"
#       "Pouring coffee into the cup\n"
#       "Pouring some milk into the cup\n"
#       "Coffee is ready!")
