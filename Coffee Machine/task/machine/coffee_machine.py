# Write your code here
drinks = int(input("Write how many cups of coffee you will need: "))
water = drinks * 200 # 200ml per drink
milk = drinks * 50 # 50ml per drink
beans = drinks * 15 # 15g per drink

print("For " + str(drinks) + " cups  of coffee you will need:\n"
                        + str(water) + " ml of water\n"
                        + str(milk) + " ml of milk\n"
                        + str(beans) + " g of coffee beans")

# print("Starting to make a coffee\n"
#       "Grinding coffee beans\n"
#       "Boiling water\n"
#       "Mixing boiled water with crushed coffee beans\n"
#       "Pouring coffee into the cup\n"
#       "Pouring some milk into the cup\n"
#       "Coffee is ready!")
