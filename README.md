# Python REST API Assignment 2
A program that performs 4 different "GET" requests, each with different query parameters, on a mock JSON file which holds 5 different tweets. Each tweet has multiple values, such as creation date, tweet ID, tweet content, username and more. 

The 1st API gets the creation time, id, and tweet text of all the tweets available in the file.

The 2nd API gets a list of all external links - all links that appear in tweet text field -  using regular expressions to extract the links and grouping the links based on tweet ids.

The 3rd API gets the tweet creation date, text, and username details about a given tweet (given the tweet’s id).

The 4th API gets detailed profile information: location, description, followers count, and friends count. Info is collected given the Twitter user's username.

This program was written in Python, utilizing the "json", "requests", and "re" built-in libaries.

# How To Run
## General Rules
Each file is titled with the appropriate API number, so run each file individually.

No external libraries were downloaded for this project.

Link to mock JSON file(provided by Dr. Hassan): (https://foyzulhassan.github.io/files/favs.json)

Download project as ZIP file and open each file in your preferred IDE.

## Python Download

## Linux
If you are using Ubuntu 16.10 or newer, then you can easily install Python 3.6 with the following commands:

```bash
$ sudo apt-get update
$ sudo apt-get install python3.6
```

## Windows
Go to the following link and download the appropriate Python version for your machine:

(https://www.python.org/downloads/)

## Mac OS
Go to the following link and download the appropriate Python version for your machine:

(https://www.python.org/downloads/macos/)

