money = int(input())
chicken = 23
goat = 678
pig = 1296
cow = 3848
speep = 6769

if money >= speep:                  # Sheep
    animals = money // speep
    print(animals, "sheep")
elif money >= cow:                  # Cows
    animals = money // cow
    print(animals, "cow" if animals == 1 else "cows")
elif money >= pig:                  # Pigs
    animals = money // pig
    print(animals, "pig" if animals == 1 else "pigs")
elif money >= goat:                 # Goats
    animals = money // goat
    print(animals, "goat" if animals == 1 else "goats")
elif money >= chicken:              # Chicken
    animals = money // chicken
    print(animals, "chicken" if animals == 1 else "chickens")
else:
    print("None")
