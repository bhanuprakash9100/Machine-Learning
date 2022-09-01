from statistics import median
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(ages)
print('The minimum age in the list is: ', min(ages))
print('The maximum age in the list is: ', max(ages))
ages.insert(0, min(ages))
ages.insert(10, max(ages))
print('The new list is: ', ages)
print('The median of the given above list is :', median(ages))
print('Average of the above list is: ', sum(ages))
range_age = max(ages) - min(ages)
print('The range is: ', range_age)




