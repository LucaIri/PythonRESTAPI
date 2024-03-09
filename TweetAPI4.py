#Author: Luca Irimie
#Date: 03-10-2024
#Purpose: Assignment 2 CIS 376 Dr. Hassan Foyzul
#API #4: (from assignment)Get detailed profile (location, description, followers_count,
#        friends_count) information about a given Twitter user (given the user’s screen name).

#JSON library to parse file
import json
#Library for api 
import requests

#API call to get values from 'favs.json'
response = requests.get("https://foyzulhassan.github.io/files/favs.json")
#Load JSON file into a single list object
response_json = json.loads(response.text)

#List of valid usernames
username_list = ["timoreilly", "MarkUry", "zephoria", "SarahPrevette", "johnmaeda"]

#Input for twitter user screen_name
User_scrn_nm = input("Enter Username(type \"q\" to quit): ")

#wHILE LOOP to constantly re-prompt if user wishes to quit
while User_scrn_nm != "q":
    while User_scrn_nm not in username_list:
        print("Invalid username; Please try again: ")
        User_scrn_nm = input("Enter Username: ")

    #iterator var
    count = 0

    #variable holding tweet number for use when matching screenname to tweet
    tweetnum = 0

    for tweet in response_json:
        if User_scrn_nm == response_json[count]['user']['screen_name']:
            break
        count+=1
    #Variables to store info
    screenname = response_json[count]['user']['screen_name']
    location = response_json[count]['user']['location']
    desc = response_json[count]['user']['description']
    followercount = response_json[count]['user']['followers_count']
    friendcount = response_json[count]['user']['friends_count']

    #Output info
    print("{}'s Profile Details: ".format(screenname))
    print("     Location: {}".format(location))
    print("     Description: {}".format(desc))
    print("     # of Followers: {}".format(followercount))
    print("     # of Friends: {}".format(friendcount))
    
    #reprompt user
    User_scrn_nm = input("Enter Username(type \"q\" to quit): ")