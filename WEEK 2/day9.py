#NESTED DATA(Lists inside dictinaries)

week_log = [{"day":"monday","steps":9200,"protocal":"OMAD"},
            {"day":"tuesday","steps":10500,"protocal":"2MAD"},
            {"day":"wednesday","steps":8800,"protocal":"Autophagy marathon"},
            {"day":"thursday","steps":11000,"protocal":"Autophagy marathon"},
            {"day":"friday","steps":7600,"protocal":"OMAD"}]

total = 0
for log in week_log:
    print(log["day"],"|",log["steps"], "steps |",log["protocal"])
    total += log["steps"]

average = total // len(week_log)
print()
print("average steps", average)
