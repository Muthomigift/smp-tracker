#working with csv files
import csv, io

csv_data = """day,steps,protocol
Monday,9200,OMAD
Tuesady,7200,2MAD
Wednesday,10500,OMAD
Thursday,4200,OMAD
Friday,8800,Autophagy marathon
Saturday,11000,2MAD
Sunday,9600,OMAD"""

f =io.StringIO(csv_data)
reader = csv.DictReader(f)

valid_steps = []
for row in reader:
    steps = int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps)
        print(f"{row['day']}: {steps} steps ({row['protocol']})")
    else:
        print(f"{row['day']}: {steps} steps -flagged as invalid.")

avg = sum(valid_steps)/len(valid_steps)
print(f"\nAverage (valid days): {round(avg)} steps")
