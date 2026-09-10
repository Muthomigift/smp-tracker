import pandas as pd

df =pd.DataFrame({
    "day": ["mon","tue","wed","thur","fri","sat","sun"],
    "steps": [9200,10500,8800,11000,7600,9400,10200],
    "sleep_hr": [7.5,8.0,6.5,7.0,9.0,7.5,8.0],
    "water_glasses": [7,8,6,9,8,7,8],
    "protocol": ["OMAD","2MAD","OMAD","OMAD","2MAD","OMAD","OMAD"]
})

#bollean column: did we hit the step goal?
df["hit_goal"] = df["steps"] >= 10000

#numeric column: steps defficit or surplus vs 10k goal
df["steps_vs_goal"] = df["steps"] - 10000

#category column: water rating
df["hydration"] = df["water_glasses"].apply(lambda x: "Good" if x >= 8 else "Low")

print(df[["day","steps","hit_goal","steps_vs_goal","hydration"]].to_string())