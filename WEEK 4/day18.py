#working with JSON
import json

week_report = {
    "name":"Chokera","steps":[9200,10500,8800,11000,7600],
    "protocols":["OMAD","2MAD","OMAD","Autophagy marathon","OMAD"]
}
#convert to JSON
json_str = json.dumps(week_report, indent=2)
print("JSON Output:")
print(json_str)

#load it back and calculate average
loaded = json.loads(json_str)
avg = sum(loaded['steps'])/len(loaded['steps'])
print("\nAfter loading back")
for key, value in loaded.items():
    print(f"\n{key}: {value}")
print(f"\nAverage steps for {loaded['name']}: {round(avg)}")