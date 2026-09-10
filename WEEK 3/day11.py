def day_report(steps, water, protocal):
    print("---Daily report---")
    print(f"steps   :{steps}")
    print(f"Water   :{water} glasses")
    print(f"Protocal:{protocal}")
    print()

def hit_goal(steps):
    return steps >= 8000

day_report (9200, 8, "OMAD")
day_report (7500, 6, "2MAD")
day_report (11000, 9, "Autophagy marathon")

print("Goal hit (9200)?", hit_goal(9200))
print("Goal hit (7500)?", hit_goal (7500))
print("Goal hit (11000)?", hit_goal (11000))