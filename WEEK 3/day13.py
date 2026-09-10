#modules and importing
import random
import math

def generate_week():  
     days=["Mon","Tue","Wed","Thur","Fri","Sat","Sun"]
     total=0
     days_on_goal=0

     for day in days:
        steps = random.randint(6000,12000)
        total +=steps
        if steps >= 8000:
            days_on_goal +=1
        print(f"{day} :{steps} steps")

     avg = math.floor(total/7)
     print(f"\nAverage steps: {avg}")
     print(f"Days on goal: {days_on_goal}/7")

generate_week()
