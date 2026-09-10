#day 3 assignment on oparators and calculations

number_of_exercises = 6
sets_per_exercise = 4
reps_per_set = 10
average_weight_per_rep = 60
session_duration_in_minutes = 45 

total_sets = number_of_exercises*sets_per_exercise
total_reps = total_sets*reps_per_set
total_volume = total_reps*average_weight_per_rep
reps_per_minute = total_reps//session_duration_in_minutes

print(f"total sets: {total_sets}")
print(f"total reps: {total_reps}")
print(f"total volume: {total_volume}kg")
print(f"reps per minute: {reps_per_minute}")
print(f"does the total volume lifted exceed 10000 kg?:", total_volume > 10000)