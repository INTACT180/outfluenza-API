#If its still up view the website!
https://outfluenza-mango.firebaseapp.com/

#DevPost Link
https://devpost.com/software/outfluenza-xmtew3

# outfluenza-API
API calls utilized in the outfluenza application for mango hacks.. Winner of Best Design at mango hacks 2018


#What it does
Outfluenza gives you a full understanding on the effect the flu has in your community, city and state, and helps the user find ways within their communities to treat the disease.

These specific API calls utlize the current information regarding your state and location to return relevant flu related data to you.

#How it works

def getNClosestTweets( lat1, lon1, n)

This function utilizes the http://flutrack.org/ API to pull tweets of people nearby with flu like symptoms. Simply call it with your latitude, longitude, and the number of tweets you wish to pull.

def getMostRecentCdcData(state):

This function pulls the recent cdc flu infection level data for your state. If the information is out of date it will write the new information to the server... Updates weekly. 

def writeRecentCdcData():

This function writes the recent cdc data to files that can be quickly accessed later. Its expensive and time consuming to do this so if this data needs to be written expect a latency of 8s. Good thing is it will only update weekly so low impact to user.

def getGoogleTrendsData(geoCode):

Get google trend data for your state to figure out which comunites around you have been searching for the flu the most frequently. geoCode is of the form 'US-(short state name)' aka 'US-FL'



