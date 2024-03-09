#Author: Luca Irimie
#Date: 03-10-2024
#Purpose: Assignment 2 CIS 376 Dr. Hassan Foyzul
#API #3: (from assignment)Get the details (tweet created_at, text, user screen_name)
#        about a given tweet (given the tweet’s id).

#JSON library to parse file
import json
#Library for api 
import requests

#API call to get values from 'favs.json'
response = requests.get("https://foyzulhassan.github.io/files/favs.json")
#Load JSON file into a single list object
response_json = json.loads(response.text)

# API 3: Get following parameters: created_at, text, screen_name, from a GIVEN input id(hint: input())
input_id = input("Input tweet ID: ")
input_id_str = str(input_id)
#print(input_id_str)

#counter vairable for iteration
count = 0

for tweet in response_json:
    if (response_json[count]['id_str']==input_id_str):
        print("Tweet Found!")
        print("     Posted on: {}".format(response_json[count]['created_at']))
        print("     Content: {}".format(response_json[count]['text']))
        print("     Username: {}".format(response_json[count]['user']['screen_name']))
    count+=1