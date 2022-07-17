#!/usr/bin/env python3

import json
import re


#check that number is in proper format with regular expression
def input_phone_number():
    phone = input('Enter the phone number: ')
    checked = re.search('\d{10}',phone)
    if checked:
        return phone
    

#check that email address is in the proper format with regular expression
def input_email_address():
    pass

#check that zipcode is in the proper format with a regular expression
def input_zip_code():
    pass

#check for correct state abbreviation
def input_state_abreviation():
    pass


# read in the json client list as dictionary
with open('clients.json', "r") as f:
    client_list = json.loads(f.read())
print(client_list)

# add new client to dictionary


new_client = {"first_name": input('Enter first name: '),
              "last_name": input('Enter last name: '),
              "street_address": input('Enter street address: '),
              "city": input('Enter city: '),
              "state": input('Enter state: '),
              "zip_code" : input('Enter zip code: '),
              "phone_number" : input_phone_number(),
              "e_mail" : input('enter email address')
              }

print(new_client["first_name"])
client_list.append(new_client)
print(client_list[1])

# write out update client list to json file
updated_clients = json.dumps(client_list, indent=4)
with open('clients.json', "w") as f:
    f.write(updated_clients)
