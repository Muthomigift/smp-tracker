import pandas as pd

df = pd.DataFrame({
    "name": ["James","Sandra","Patrick","Grace","Brian","Kevin","James","Grace","Sandra","James"],
    "protocol": ["OMAD","2MAD","OMAD","OMAD","2MAD","OMAD","OMAD","OMAD","2MAD","OMAD"],
    "city": ["Nairobi","Mombasa","Nairobi","Kisumu","Nairobi","Mombasa","Nairobi","Kisumu","Mombasa","Nairobi"],
})

print("Protocol distribution:")
print(df["protocol"].value_counts())

print("\nName distribution:")
print(df["name"].value_counts())

print("City distribution:")
print(df["city"].value_counts())