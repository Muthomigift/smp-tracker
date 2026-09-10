print("Exercise for loops.")

#use a for loop to print each day count and if met the 8000 step target
daily_step_count = [8200,5100,11300,6800,9400,4200,10100]
target = 8000
day = 0

for steps in daily_step_count:
    print("Day" ,day,steps, "steps done")
    if steps >= target:
        print("Wow," ,steps,"done, Target of" ,target, "hit.")
    else:
        print("Target missed by" ,target-steps, "Keep up.")
        day = day+1

#use continue to skip any day belo 5000 steps when calculating weekly average
daily_step_count = [8200,5100,11300,6800,9400,4200,10100]
target = 5000
weekly_target_met_steps =0
active_days =0

for steps in daily_step_count:
    if steps < target:
        print("skipped step" ,steps,)
        continue #this skips a value thet is less than 5000 and reads the next value
    print("above 5000 steps" ,steps,)

print("weekly total steps above" ,weekly_target_met_steps,)
print("total active days" ,active_days,)
print("average weekly steps" ,weekly_target_met_steps // steps)
active_days += 0
weekly_target_met_steps += 0