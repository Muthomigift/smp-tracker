#DICTIONARIES

my_log ={"steps":2500, "water_glasses":7, "fasting_protocal":"OMAD", "cold_shower":True,
          "sleep_hours":8}
print("My log")
for key, value in my_log.items():
    print(f"{key} : {value}") #alternative: print(key ":" value)
print()

if my_log["steps"] >= 8000:
    print("Steps target hit.")
else:
    print("steps target missed")



