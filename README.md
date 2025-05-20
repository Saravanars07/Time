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
