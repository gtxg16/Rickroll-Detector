import requests
from sys import exit  # required for pyinstaller to compile

while True:
    user_input = input("Enter link (or enter 'q' to exit): ")
    if user_input == 'q':
        exit()
    else:
        pass
    rickroll = ['dQw4w9WgXcQ', 'QtBDL8EiNZo', 'iik25wqIuFo', 'j5a0jTc9S10', 'xfr64zoBTAQ', 'LjQZaD9EEJ0', 'V-_O7nl0Ii0', 'cvh0nX08nRw', 'gokdrC4gQA4', 'rr.noordstar.me', 'lasesp.com/article', 'thisworldthesedays.com', 'theraleighregister.com', 'latlmes.com/breaking', ]
    if any(substring in user_input for substring in rickroll):  # if any part of url matches any element in list
        print("This link is a rickroll, don't click it!")
    else:
        try:
            r = requests.get(user_input)  # see where shortened link leads
        except requests.exceptions.MissingSchema:  # except if input is not url
            print("This isn't a valid link...")  # it would have already gone on to else since it didnt have one of the elements in the list
            exit()
        if any(substring in r.history for substring in rickroll):  # checking if final link that shortened url leads to is a rickroll
            print("This link is a rickroll, don't click it!")
        else:
            print("This link is not a rickroll, it is safe to click it!")
