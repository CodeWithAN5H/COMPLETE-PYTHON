# 2dlist example = [list1, list2, list3]

fruits =     ["apple", "orange", "banana", "coconut"]
vegetables = ["celery", "carrots", "potatoes"]
meats =      ["chicken", "fish", "turkey"]

groceries = [fruits, vegetables, meats]

for collection in groceries:
    for food in collection:
        print(food)