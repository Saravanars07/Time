# Collect user inputs
distance = float(input("Enter total distance in kilometers: "))
speed = float(input("Enter vehicle speed in km/h: "))

try:
    # Calculate time in decimal hours
    hours_decimal = distance / speed
    # Convert to total minutes and split into hours/minutes
    total_minutes = round(hours_decimal * 60)
    hours, minutes = divmod(total_minutes, 60)

    # Format output based on calculated values
    if hours == 0:
        print(f"It will take {minutes} minutes.")
    elif minutes == 0:
        print(f"It will take {hours} hours.")
    else:
        print(f"It will take {hours} hours and {minutes} minutes.")

except ZeroDivisionError:
    print("Error: Speed cannot be zero. Please enter a valid speed.")
