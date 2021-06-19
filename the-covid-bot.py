import tweepy
from datetime import datetime
import json
import urllib.request
import time
import os.path

# api login details for tweepy
CONSUMER_KEY = 'lk3tYCoi18XqtRnJqwMsJiQ4O'
CONSUMER_SECRET = 'jHrr9ixsq4V5ziVdhZakaAzxQuRLYWN6N2HBkaQitbZCCVc4it'
ACCESS_KEY = '1403541059632873477-Nq7qoYZxt21idE3iiCGE4oOEJPWNxn'
ACCESS_SECRET = '7blv9zwieHzHnY30cXGtGZDmVqcBHCQRtsjyOg6XvlQiI'

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
# login

api = tweepy.API(auth) 
url = "https://api.covid19tracker.ca/summary"
fileobj = urllib.request.urlopen(url)
data = json.loads(fileobj.read())
    

print('This is my twitter bot!')
print(json.load(urllib.request.urlopen(url)))
while True:
    print(data['data'])

    # save the data from the json into variables to print to console and tweet
    for record in data['data']: 
        print(record)
        new_deaths = int(record['change_fatalities'])
        new_vaccinations = int(record['change_vaccinated'])
        update_cases = int(record['change_cases'])
        update_hospitalizations = int(record['change_hospitalizations'])
        total_cases = int(record['total_cases'])
        total_deaths = int(record['total_fatalities'])
        total_tests = int(record['total_tests'])
        total_current_vaccinated = int(record ['total_vaccinated'])
        total_recoveries = int(record['total_recoveries'])
        total_new_vaccinated = int(record['total_vaccinations'])
        total_vaccines_distributed = int(record['total_vaccines_distributed'])


    # the tweets to be published !!
    tweet = ("Canadian Covid Statistics For Today:" + "\n\nNew Cases: " + str(update_cases) + "\nNew Deaths: " + '{:,}'.format(new_deaths) + "\n\nTotal Cases: " + '{:,}'.format(total_cases) + "\nTotal Deaths: " + '{:,}'.format(total_deaths) + "\nTotal Tests: " + '{:,}'.format(total_tests) + "\nTotal Recoveries: " + '{:,}'.format(total_recoveries) + "\n\nNew Vaccinations: " + '{:,}'.format(new_vaccinations) + "\nTotal Canadians Vaccinated: " + '{:,}'.format(total_current_vaccinated) + "\nRemaining Vaccine Supply: " + '{:,}'.format(total_new_vaccinated))
    tweet2 = ("Please follow the recommended health precautions when travelling or working: https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/prevention-risks.html")

    #check character amount for the tweet, must be 280 or below, edit if there is too much
    print(len(tweet)) 

    #ensure output is looking good in the console before tweeting
    print(tweet) 

    # change directory to pictures
    os.chdir('pics')


    # iterate through the pictures in the 'pics' directory and couple it with a tweet

    try:
        for picture in os.listdir('.'):
            api.update_with_media('../8.jpg', tweet2) #go to previous directory to retreive picture
            api.update_with_media(picture, tweet)
            time.sleep(86400) # 86400 seconds = every 24 hours

    except:
            print('There was an error with uploading the tweets')
            break

