import pandas as pd

data = {
    "day": ["Mon","Tue","Wed","Thur","fri","Sat","Sun"],
    "steps": [9200,10500,8800,11000,7600,9400,10200],
    "sleep_hr": [7.5,8.0,6.5,7.0,9.0,7.5,8.0],
    "protocol": ["OMAD","2MAD","OMAD","OMAD","2MAD","OMAD","OMAD"],
    "cold_shower": [True,True,False,True,True,True,True]
}

df = pd.DataFrame(data)
print(df.to_string())

print("shape (rows, cols):", df.shape)
print("\nColumns:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nFirst three rows:")
print(df.head(3).to_string())

#INSPECTING COLUMNS
print("\nSteps column")
print(df["steps"])
print("\nSteps and protocol")
print(df[["steps","protocol"]].to_string())

#ROW SELECTION WUTH ILOC AND LOC
print("\nFirst row (iloc[0]:)")
print(df.iloc[0])
print("\nRow 0 to 2 (iloc[0:3]):")
print(df.iloc[0:3].to_string)
print("\nLast row")
print(df.iloc[-1])