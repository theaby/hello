"""Running Streak - Calculate the difference between two dates in years, months and days"""
import sys
import datetime

# define the date format
DATE_FORMAT = "%m/%d/%Y"

CORRECT_DATE = 0
while CORRECT_DATE == 0:
    # input data to capture
    START_DATE = input("Enter the start date in the month/day/year format: ")
    END_DATE = input("Enter the end date in the month/day/year format: ")

    if START_DATE > END_DATE:
        print("The start date must be less than the end date.")
        print("Let's try this again \n")
    elif START_DATE < END_DATE:
        CORRECT_DATE == 1
        break
    else:
        print("There was an issue with the date, please try again in the perscribed format")


# convert the string to date format
START_DATE = datetime.datetime.strptime(START_DATE, DATE_FORMAT)
END_DATE = datetime.datetime.strptime(END_DATE, DATE_FORMAT)

# Calculations
DIFF_IN_DAYS = END_DATE - START_DATE
YEARS_RUN = DIFF_IN_DAYS.days//365
REMAINING_DAYS = DIFF_IN_DAYS.days - (YEARS_RUN * 365)

# Output
print(f"\nHe's been running for {DIFF_IN_DAYS.days} days")
print(
    f"This means {YEARS_RUN} years and {REMAINING_DAYS} days.")

EXIT_KEY = input(
    "\n\nHit enter to exit: ")
if EXIT_KEY == "098aslkj..":
    sys.exit()
else:
    sys.exit()
