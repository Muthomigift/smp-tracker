#LISTS: Sorting multiple values.

week_steps = [9200,7400,10500,8800,6900,11000,9600]
target = 8000
day = 1

for steps in week_steps:
    if steps >= 8000:
        print("Day" ,day, "Good work," ,steps, "steps done, target hit")
    else:
        print("Day" ,day, steps, "steps -Target missed. Extra work needs to done")
    day = day+1
print("Total days tracked:" ,len(week_steps))
