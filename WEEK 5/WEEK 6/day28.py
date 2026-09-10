import pandas as pd

df = pd.DataFrame ({
    "day": ["mon","tue","wed","thur","fri","sat","sun"],
    "steps": [9200,10500,8800,11000,7600,9400,10200],
    "sleep_hr": [7.5,8.0,6.5,7.0,9.0,7.5,8.0],
    "protocol": ["OMAD","2MAD","OMAD","OMAD","2MAD","OMAD","OMAD"]
})

#AVERAGE STEPS PER FASTING PROTOCOL
grouped = df.groupby("protocol")["steps"].mean().round(0)
print("Average steps by protocol")
print(grouped)

print()
#total steps per protocol
totals = df.groupby("protocol")["steps"].sum()
print("Total steps by protocol:")
print(totals)