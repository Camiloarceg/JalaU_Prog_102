#!/usr/bin/env python3
"""
    Password Generator Script
"""


import random
import string

# variable to print the password
password = ""

# information request
app_name = input("For which application do you want your password? ")
char_num = input("how many characters should be on your password? ")

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

# print password message
print(f"The password for {app_name} is {password}")
