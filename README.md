# Time

# Distance Time Cal

This Python script calculates the time taken to travel a certain distance at a given speed. It takes user inputs for distance and speed, then computes and displays the travel time in hours and minutes.

***Features***
  - User Input: Prompts the user to enter distance and speed.  
  - Calculation: Computes the total travel time. 
  - Output: Displays the time in hours and minutes.


***How to Use***
  1. Run the Script:
      Execute the script in your Python environment.
  2. Enter Distance:
      When prompted, input the total distance you want to travel (in units such as kilometers or miles).
  3. Enter Speed:
      When prompted, input the speed at which you will travel (in the same units per hour).
  4. View Result:
      The script will display the time taken to cover the distance at the given speed in hours and minutes.

***Example***

```
Enter a Distance: 150
Enter a Speed: 60
Time taken for total distance: 150 at speed: 60 in a time 2 hours and 30 minutes
```
***Formula Used***

The calculation is based on the formula:

```
Time = Distance / Speed
```

***Script Code***

```
Distance = int(input("Enter a Distance:"))
Speed = int(input("Enter a Speed:"))

cal = Distance / Speed
hours = int(cal)
minutes = int((cal - hours) * 60)
print(f"Time taken for total distance:{Distance} at speed :{Speed} in a time {hours} hours and {minutes} minutes")

```
***Notes***

  - The program only accepts integer inputs
  - For more precise calculations, you may want to modify the script to accept floating-point numbers
  - Ensure that both distance and speed are entered in compatible units (e.g., kilometers and kilometers per hour).
  - The script does not handle cases where speed is zero or negative. Add error handling for production use.

# Time Distance Cal

This Python script calculates the time required to travel a user-specified distance at a given speed. The result is displayed in hours and minutes, with user-friendly formatting and error handling for invalid input.

***Features***

  - Precise Input Handling: Accepts decimal values for distance and speed
  - Error Handling: Catches division by zero when speed is 0
  - Smart Output Formatting:
      - Shows only minutes if under 1 hour
      - Shows only hours if exact hours
      - Shows combined format otherwise
  - Accurate Rounding: Converts to total minutes first to avoid floating-point rounding errors.

***How to Use***

  1. Run the Script:
  Start the script in your Python environment (Python 3.x recommended).
  2. Input Distance:
  Enter the total distance you wish to travel (in kilometers).
  3. Input Speed:
  Enter the vehicle speed (in kilometers per hour).
  4. View Result:
  The script will display the travel time in an easy-to-read format.

***Usage***
  1. Run the script
     ```
     python Time distance Cal.py
     ```
  2. Enter:
      - Distance in kilometers.
      - Speed in km/h.
  3. View the calculated travel time.

***Example***

```
Enter total distance in kilometers: 120
Enter vehicle speed in km/h: 80
It will take 1 hours and 30 minutes.
```
***If the speed is zero:***

```
Enter total distance in kilometers: 100
Enter vehicle speed in km/h: 0
Error: Speed cannot be zero. Please enter a valid speed.
```

***Script Code***

```
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
```
***Notes***

  - Units: Ensure both distance and speed are in kilometers and kilometers per hour, respectively.
  - Input Validation: The script handles zero speed, but does not check for negative or non-numeric input. For production use, consider adding further input validation.
  - Rounding: Travel time is rounded to the nearest minute.
