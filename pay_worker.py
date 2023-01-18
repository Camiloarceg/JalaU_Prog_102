#!/usr/bin/env python3


def calculate_pay(hours, rate, employee):
    # calculate employee's payment
    if hours <= 40:
        payment = hours * rate
    else:
        payment = hours * rate + (hours - 40) * rate * 0.5
    print(f"{employee} payment is: {payment}")


with open("employees.csv") as file:
    # get all employees without the header of the CSV file
    for line in file.readlines()[1:]:
        words = line.strip().split(",")

        if words[0] != "":
            words[2].replace(".", ",")
            calculate_pay(float(words[1]), float(words[2]), words[0])
    # print(words)
