import pandas as pd

df = pd.DataFrame({
    "name": ["James Omondi","Sandra Weru","Patrick Njiru","Grace Achieng","Brian Kamau","Kevin Mwangi"],
    "steps": [9200,10500,8100,11000,7400,10800],
    "sleep_hr": [7.5,8.0,6.5,7.0,9.0,7.5]
})

#sort by steps, highest first
ranked =df.sort_values("steps",ascending=False).reset_index(drop=True)
ranked.index = ranked.index +1 #1-based key
print("Steps leaderboard")
for i, row in ranked.iterrows():
    print(f"#{1} {row['name']:<20} {row['steps']:,} steps")