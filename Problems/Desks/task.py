from math import ceil
# put your python code here
class_1 = int(input())
class_2 = int(input())
class_3 = int(input())

total_desks = ceil(class_1 / 2) + ceil(class_2 / 2) + ceil(class_3 / 2)
print(total_desks)
