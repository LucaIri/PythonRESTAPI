#Author: Luca Irimie
#Date: 03-10-2024
#Purpose: Assignment 2 CIS 376 Dr. Hassan Foyzul
#API #2: Get a list of all external links (all links that appear in tweet text field.
#        Use regular expressions to extract the links , the links should be grouped based on tweet ids)

#JSON library to parse file
import json
#Library for api 
import requests
#Library for reg expressions
import re

#API call to get values from 'favs.json'
response = requests.get("https://foyzulhassan.github.io/files/favs.json")
#Load JSON file into a single list object
response_json = json.loads(response.text)

#Counter variable to step through tweets in file
count =0

#For loop, loads tweet text into a 'strng'. findall() uses reg expression to search 'strng' for URLs and saves list in 'urls'.
#If 'urls' is empty, display empty message
#Else, display URLs found and tweet ID
for tweet in response_json:
    strng = response_json[count]['text']
    #strng = "hello world"   // used to test empty list of URLs
    urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', strng)
    #print(urls)
    if not urls:
        print("External URLs not found in tweet #{}".format(response_json[count]['id_str']))
    else:
        print("URL(s) found in tweet ID#: {}: ".format(response_json[count]['id_str']), urls)
    count+=1