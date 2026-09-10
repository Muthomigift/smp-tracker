#combining nested data into one clean record(FUUL PARSE AND FLATTEN)
raw_members = [
    {
        "profile":{"name":"James Omondi","city":"Nairobi"},
        "metrics":{"steps":9200,"sleep_hours":7.5,"bench_press_kg":80},
        "discipline":{"cold_shower":False,"protocol":"OMAD"}
    },
    {
        "profile":{"name":"Grace Achieng","city":"Nairobi"},
        "metrics":{"steps":11000,"sleep_hours":7.0,"bench_press_kg":60},
        "discipline":{"cold_shower":False,"protocol":"OMAD"}
    },
    {
        "profile":{"name":"Brian Kamau","city":"Kisumu"},
        "metrics":{"steps":7400,"sleep_hours":9.0,"bench_press_kg":70},
        "discipline":{"cold_shower":True,"protocol":"2MAD"}
    }
]

#flatten each nested record into one clean dictionary
flattened = []
for m in raw_members:
    record ={
        "name":        m["profile"]["name"],
        "city":        m["profile"]["city"],
        "steps":       m["metrics"]["steps"],
        "sleep":       m["metrics"]["sleep_hours"],
        "bench":       m["metrics"]["bench_press_kg"],
        "protocol":    m["discipline"]["protocol"],
        "cold shower": m["discipline"]["cold_shower"]
    }
    flattened.append(record)
print("AFTER FLATTENNING")
print(flattened)

for r in flattened:
    shower = "yes" if r["cold shower"] else "no"
    print(f"\n{r['name']},{r['city']}:{r['steps']} steps, {r['protocol']}, shower ={shower}")
