import requests
from sys import exit

while True:
    user_input = input("Enter link (or enter 'q' to exit): ")
    if user_input == 'q':
        exit()
    else:
        pass
    rickroll = ['dQw4w9WgXcQ', 'QtBDL8EiNZo', 'iik25wqIuFo', 'j5a0jTc9S10', 'xfr64zoBTAQ', 'LjQZaD9EEJ0', 'V-_O7nl0Ii0', 'cvh0nX08nRw', 'gokdrC4gQA4']
    if any(substring in user_input for substring in rickroll):
        print("This link is a rickroll, don't click it!")
    else:
        try:
            r = requests.get(user_input)
        except requests.exceptions.MissingSchema:
            print("This isn't a valid link...")
            exit()
        if any(substring in r.url for substring in rickroll):
            print("This link is a rickroll, don't click it!")
        else:
            print("This link is not a rickroll, it is safe to click it!")
