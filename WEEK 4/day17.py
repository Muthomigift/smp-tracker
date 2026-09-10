#ERROR HANDLING
def safe_data_log(data):
    try:
        steps = int(data["steps"])
    except(ValueError,TypeError,KeyError):
        print("Invalid steps data. Skipping entry.")
        return None

    water = data.get("water", 0)
    protocal = data.get("protocal", "unknown")

    print(f"Steps: {steps}|Water {water} glasses |Protocal {protocal}")
    return steps

entries =[{"steps":"9200", "water":8, "protocal":"OMAD"},
          {"steps":"bad", "water":7, "protocal":"2MAD"},
          {"steps":"8800", "protocal":"OMAD"},
          {"steps":"11000", "water":9}]

results = [safe_data_log(e) for e in entries]
valid = [r for r in results if r is not None]
print(f"\n Valid entries: {len(valid)}")

