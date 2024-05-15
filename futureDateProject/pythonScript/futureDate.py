# import modules 
from datetime import timedelta, datetime
from time import sleep


# welcome message 
print("Welcome! Calculate future date in number, e.g. in 7days time.")
# sleep to read 
sleep(5)

def calculator():    
    
    # number of days to add 
    try:
        numbers = int(input('Enter the number of days: '))
    except ValueError:
        print("Please enter a valid number")

    convertToDate = timedelta(days=numbers)
    future_date = current_date + convertToDate
    print(f"{numbers} days from now, will be {future_date.strftime('%B-%d-%Y')}.")


# call current date 
knowDate = True
while knowDate:
    # currentDate 
    current_date = datetime.now()
    
    # extract year, month and day 
    current_year = int(current_date.strftime('%Y'))
    current_month = int(current_date.strftime('%m'))
    current_day = int(current_date.strftime('%d'))

    # convert back to date format 
    current_date = datetime(year=current_year, month=current_month, day=current_day)

    # function call 
    calculator()
    
    continueProgram = input(" To check another future date: Enter - 'Y'\n To exit: Enter -'N'. " ).lower()
    
    if continueProgram == 'y':
        continue
    elif continueProgram == 'n':
        knowDate = False
        sleep(2)
        print("Stay positive")
    else:
        print("Please enter a valid input")