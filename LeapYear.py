# Prompt the user to input a year
year = int(input("Enter a year: "))

# Check if the year is a leap year
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    leap_year = True
else:
    leap_year = False

# Display the result
if leap_year:
    print(year, "is a leap year.")
else:
    print(year, "is not a leap year.")
