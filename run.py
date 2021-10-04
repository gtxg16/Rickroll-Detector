from requests import get as checkshorten

user_input = input("Enter link: ")
rickroll = ['dQw4w9WgXcQ', 'QtBDL8EiNZo', 'iik25wqIuFo', 'j5a0jTc9S10', 'xfr64zoBTAQ', 'LjQZaD9EEJ0', 'V-_O7nl0Ii0', 'cvh0nX08nRw', 'gokdrC4gQA4']

if any(substring in user_input for substring in rickroll):
    print("This link is a rickroll, don't click it!")
else:
    r = checkshorten(user_input)
    if any(substring in r.url for substring in rickroll):
        print("This link is a rickroll, don't click it!")
    else:
        print("This link is not a rickroll, it is safe to click it!")
