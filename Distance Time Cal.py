Distance=int(input("Enter a Distance:"))
Speed=int(input("Enter a Speed:"))

cal=Distance/Speed
hours=int(cal)
minutes=int((cal-hours)*60)
print(f"Time taken for total distance:{Distance} at speed :{Speed} in a time {hours} hours and {minutes} minutes")