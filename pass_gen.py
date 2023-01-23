#!/usr/bin/env python3
"""
    Password Generator Script
"""


import random
import string
import csv
import base64


def add_password(app_name, password, path):
    """Add a new encoded password to csv file."""

    # encode the password
    encoded_password = base64.b64encode(password.encode("utf-8"))
    print(f"encoded_password : {encoded_password}")
    #row creation
    row = [app_name.lower(), encoded_password]
    # add the encoded password to csv file
    with open(path, 'a') as csv_file:
        writer_object = csv.writer(csv_file)
        writer_object.writerow(row)

def overwrite_password(path, app_name, new_password):
    """ Overwrite the password """
    target = 0
    rows = []
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        for row in csv_reader:
            if row[0] == app_name:
                continue
            rows.append(row)
    print(rows)
    with open(path, 'w') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerows(rows)
    add_password(app_name, new_password, path)

def get_password(path, app_name):
    """ Get a  decoded password """
    with open(path, 'r') as csv_file:
        # creating a csv reader object
        csv_reader = csv.reader(csv_file)
        # extracting field names through first row
        fields = next(csv_reader)
        # extracting each data row one by one
        for row in csv_reader:
            # found the matching app
            if app_name.lower() == row[0]:
                # return the decoded password
                return base64.urlsafe_b64decode(row[1]).decode("utf-8")

def has_data_rows(path):
    """ check if the file has data rows """
    with open(path) as file:
        return file.readline() and file.readline()


def get_apps(path):
    """Return list of all apps in csv file."""
    apps = []
    # get data frame from file
    with open(path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)
        for row in csv_reader:
            print(row)
            apps.append(row[0])
    return apps


def character_assignation():
    """function to validate user input"""
    while True:
        try:
            char_num = int(
                input(
                    "Please enter the amount of characters it must be greater than 8: "
                )
            )
            if char_num < 8:
                print("Please enter a valid amount of characters")
                continue
            break
        except :
            print("Please enter only valid type of characters")
    return char_num


def generate_password(char_num):
    """generate randomize password"""
    # variable to print the password
    password = ""

    # data structures for character randomization
    char_type = ["numbers", "uppers", "lowers", "lowers", "lowers", "uppers"]

    char_dict = {
        "numbers": list(string.digits),
        "lowers": list(string.ascii_lowercase),
        "uppers": list(string.ascii_uppercase),
    }

    # generation process
    for i in range(int(char_num)):
        password += random.choice(char_dict[random.choice(char_type)])

    # return the password
    return password


if __name__ == "__main__":
    """Guard to protect the script from unwanted excecution"""

    # field names and rows
    fields = ["App Name", "Password"]
    apps = []
    path = "passwords.csv"

    while True:
        # app name request
        app_name = input("Please enter your app name: ")
        print(has_data_rows(path))
        # validate if file has data in it
        if has_data_rows(path):
            app_list = get_apps(path)
            print(app_list)
            # check if app is already created
            if app_list.count(app_name) == 0:
                char_num = character_assignation()
                password = generate_password(char_num)
                print(password)
                add_password(app_name, password, path)
            # if app is already take a decision
            else:
                decision = input("Seems you already have a password, 1 for view password or 2 for overwrite password: ")
                if decision == '1':
                    # print the retieved password
                    print(f"Your password for {app_name} is {get_password(path, app_name)}")
                else:
                    # overwrite the password
                    char_num = character_assignation()
                    new_password = generate_password(char_num)
                    overwrite_password(path, app_name, new_password)
        #if the file is empty or only with header fields
        else:
            char_num = character_assignation()
            password = generate_password(char_num)
            add_password(app_name, password, path)