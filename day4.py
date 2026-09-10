steps = 7500
sleep_hours = 6
water_glasses = 5
cold_shower = True
pages_read = 15

# steps
if steps >= 10000:
    print("steps: Excellent.")
elif steps >= 7500:
    print("steps: Good.")
else:
    print("steps: Needs improvement.")

# sleep hours
if sleep_hours >= 7:
    print("Sleep: Good.")
else:
    print("Sleep: Low, needs improvement")

# water glasses
if water_glasses >= 8:
    print("Water: Good.")
else:
    print("Water: low.")

#verdict
if steps >= 7500 and sleep_hours >=7 and water_glasses >=8:
    print("Good work.")
else:
    print("Need more effort. keep pushing>")