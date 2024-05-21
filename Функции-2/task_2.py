import random

first_list = []
second_list = []
third_list = []

for i in range(11):
    first_list.append(random.randint(1, 30))
    second_list.append(random.randint(1, 30))

print(first_list)
print(second_list)

tempList = first_list
third_list = list(filter(lambda num: False if num in tempList else True, second_list))

tempList = second_list
third_list += list(filter(lambda num: False if num in tempList else True, first_list))

print(third_list)
