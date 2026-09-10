#LIST METHODS
steps = [8800,6500,11000,9200,7300]
print("Steps:",steps)
#adding a number in the list
steps.append(10500)
print("After adding 10500 in the list:", steps)
#removing a number in the list
steps.remove(6500)
print("After removing 6500:",steps)
#sorting the list from highest to lowest
steps.sort(reverse=True)
print("after sorting highest to lowest",steps)
#how many days exceed 9000 steps
days_above_9000 = 0
for steps in steps:
    if steps >= 9000:
        days_above_9000 += 1
print("days above 9000 steps=",days_above_9000)
    