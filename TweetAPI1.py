#Author: Luca Irimie
#Date: 03-10-2024
#Purpose: Assignment 2 CIS 376 Dr. Hassan Foyzul
#API #1: (from assignment) Get all tweets (create time, id, and tweet text) available in the archive

#JSON library to parse file
import json
#Library for api 
import requests

#API call to get values from 'favs.json'
response = requests.get("https://foyzulhassan.github.io/files/favs.json")

#Load JSON file into a single list object
response_json = json.loads(response.text)
print(type(response_json))

#Counter for tweet number
count =0

#For loop to loop through each tweet and search for tweet parameters: created-at, id_str, text
for tweet in response_json:
    print("Tweet #{}:".format(count+1))
    print("     Posted on: {}".format(response_json[count]['created_at']))
    print("     Post ID: {}".format(response_json[count]['id_str']))
    print("     Content: {}".format(response_json[count]['text']))
    count+=1

    