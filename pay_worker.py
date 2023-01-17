#!/usr/bin/env python3

# ask for hours
hours = input('Please enter the number of hours: ')
hours = int(hours)
#ask for rate
rate = input('Please enter the rate for the employee: ')
rate = int(rate)

# calculate employee's payment
if hours <= 40:
    payment = (hours * rate)  
else:
    payment = hours * rate + (hours - 40) * rate * 0.5
print(f"Employee's payment is: {payment}")
