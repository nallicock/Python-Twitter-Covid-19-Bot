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
today = datetime.today().strftime('%d/%m/%Y')#format today's date
today_time = time.strftime("%H:%M:%S")

print('This is my twitter bot!')
print(json.load(urllib.request.urlopen(url)))
print(data['data'])


# save the data from the json into variables to print to console and tweet
for record in data['data']: 
    print(record)
    new_deaths = record['change_fatalities']
    new_vaccinations = record['change_vaccinated']
    update_cases = record['change_cases']
    update_hospitalizations = record['change_hospitalizations']
    total_cases = record['total_cases']
    total_deaths = record['total_fatalities']
    total_tests = record['total_tests']
    total_current_vaccinated = record ['total_vaccinated']
    total_recoveries = record['total_recoveries']
    total_new_vaccinated = record['total_vaccinations']
    total_vaccines_distributed = record['total_vaccines_distributed']


# the tweets to be published !!
tweet = ("Canadian Covid Statistics as of " + str(today) + " | " + today_time + "\n\nNew Cases: " + str(update_cases) + "\nNew Deaths: " + str(new_deaths) + "\n\nTotal Cases: " + str(total_cases) + "\nTotal Deaths: " + str(total_deaths) + "\nTotal Tests: " + str(total_tests) + "\nTotal Recoveries: " + str(total_recoveries) + "\n\nNew Vaccinations: " + str(new_vaccinations) + "\nTotal Canadians Vaccinated: " + str(total_current_vaccinated) + "\nRemaining Vaccine Supply: " + str(total_new_vaccinated))
tweet2 = ("Please follow the recommended health precautions when travelling or working: https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection/prevention-risks.html")
print(len(tweet)) #check character amount for the tweet, must be 280 or below, edit if there is too much
print(tweet) #ensure output is looking good in the console before tweeting

# change directory to pictures
os.chdir('pics')

loop_number = 0

# iterate through the pictures in the 'pics' directory and couple it with a tweet
while True:
        try:
            for picture in os.listdir('.'):
                api.update_with_media('../8.jpg', tweet2) #go to previous directory to retreive picture
                api.update_with_media(picture, tweet)
                time.sleep(15)# 86400 seconds = every 24 hours

        except:
            print('There was an error with uploading the tweets')
            break

