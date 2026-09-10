import json

#Vs code version would add two lines:
#From openai import OpenAI
#Client = OpenAI(api_key=os.getenv("OPEN_API_KEY"))
#Then replacethe simulated_responses below with a real client.chat.completions.create() call

workshop_system = """You are a Jua Kali workshop assistant for Kamau metalworks, Gikomba.
When a client describes a job, return ONLY with these keys: item (str), material (str), days_to_complete (int), deposit_kes (int).
No other text."""

job_requests = [
    "I need a sliding gate, about 10 feet wide, mild steel.",
    "Window grills for three windows, 3*4 feet wide, mild steel.",
    "A stell door frame for a standard door, hollow tube.",
]

#Simulated AI JSON responses
simulated_responses = [
    '{"item": "window grills *3", "material": "angle iron", "est_kes": 2100, "days_to_complete": 3, "deposit_kes": 10500}',
    '{"item": "door frame", "material": "hollow tube", "est_kes": 9800, "days_to_complete": 2, "deposit_kes": 4900}',
] 

print("Kamau Metalworks: AI Quotation Assistant\n")
for request, response_json in zip(job_requests, simulated_responses):
    print(f"Client: {request}")
    quote = json.loads(response_json)
    print(f"  Item:      {quote['item']}")
    print(f"  Material:  {quote['material']}")
    print(f"  Quote:     KES {quote['est_kes']}")
    print(f"  Deposit:   KES {quote['deposit_kes']}")
    print(f"  Ready in:  {quote['days_to_complete']} days")
    print()