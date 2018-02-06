import requests
import json
import datetime
import math
import heapq
import ast
import datetime
import os
from pytrends.request import TrendReq


fluCall = 'http://flutrack.org/results.json'

def getNClosestTweets( lat1, lon1, n):

	r2 = requests.get(fluCall)
	events = json.loads(r2.text)


	R = 6371 #Radius of the Earth
	h = []
	for event in events:
		lon2 = float(event['longitude'])
		lat2 = float(event['latitude'])
		dlon = (lon2 - lon1)*math.pi/180
		dlat = (lat2 - lat1)*math.pi/180
		a = math.pow((math.sin(dlat/2)),2) + math.cos(lat1*math.pi/180) * math.cos(lat2*math.pi/180) *  math.pow((math.sin(dlon/2)),2)
		c = 2 * math.atan2( math.sqrt(a), math.sqrt(1-a) )
		d = R * c
		heapq.heappush(h, (d, event))

	output = []
	ostring = u'poopman'
	for i in range(0,20):
		temp = heapq.heappop(h)
		while(temp[1]['user_name'] == ostring):
			temp = heapq.heappop(h)
		ostring = temp[1]['user_name']
		temp[0]
		temp[1]
		output.append(temp[1])

	return output

def getMostRecentCdcData(state):
	try:
		with open('storedData/lastUpdate.txt', 'r') as f:
			lastUpdateCdc= f.readline()
			lastUpdateDate = f.readline()
			lastUpdateCdc
			datetimeCdc = datetime.datetime.strptime(lastUpdateCdc, '%b-%d-%Y\n')
			lastUpdateDate
			datetimeLastCheck = datetime.datetime.strptime(lastUpdateDate,'%b-%d-%Y')
			oneWeek = datetime.timedelta(weeks=0, days=7, hours=0, minutes=0, seconds=0)
			if(datetimeCdc.date() < datetime.datetime.today().date() - oneWeek and datetimeLastCheck.date() != datetime.datetime.today().date()):
				writeRecentCdcData()
			f.close()

	except:
		writeRecentCdcData()

	latestFile = '1988-89.txt'
	for f in os.listdir('storedData/i/'):
	    if f > latestFile:
			latestFile = f

	fileContents = ''
	with open('storedData/i/'+latestFile, 'r') as f:
		fileContents = f.read()
		f.close()

	dataset = json.loads(fileContents)

	maxWeek = -1000
	for week in dataset:
		current = int(week)
		if(current>= 40):
			current-=52
		if(current>maxWeek):
			maxWeek = current

	if maxWeek<0:
		maxWeek+=52

	dataset[str(maxWeek)][state]
	return dataset[str(maxWeek)][state]


def writeRecentCdcData():
	r2 = requests.get('https://gis.cdc.gov/grasp/fluView1/Phase1DownloadDataP/2017-2018')

	literal = ast.literal_eval(r2.text)
	events = json.loads(literal)
	events = events['datadownload']

	dataset = {}
	for event in events:
		if dataset.get(event[u'season']) == None:
			dataset[event[u'season']] = {event[u'weeknumber']:{event[u'statename']:event}}
		elif dataset[event[u'season']].get(event[u'weeknumber']) == None:
			dataset[event[u'season']][event[u'weeknumber']] = {event[u'statename']:event}
		elif dataset[event[u'season']][event[u'weeknumber']].get(event[u'statename']) == None:
			dataset[event[u'season']][event[u'weeknumber']][event[u'statename']] = event
		else:
			dataset[event[u'season']][event[u'weeknumber']][event[u'statename']] = event

	dataset["2017-18"]["4"]["Florida"]

	maxSeason= "1994-05"
	for season in dataset:
		season.encode('ascii','ignore')
		if season > maxSeason:
			maxSeason = season
		with open('storedData/i/' + season +'.txt', 'w') as f:
			f.write(json.dumps(dataset[season]))
			f.close()

	maxWeek = -1000
	for week in dataset[maxSeason]:
		current = int(week)
		if(current>= 40):
			current-=52
		if(current>maxWeek):
			maxWeek = current

	if maxWeek<0:
		maxWeek+=52

	with open('storedData/lastUpdate.txt', 'w') as f:
		f.write(dataset[maxSeason][str(maxWeek)]["Florida"]['weekend'].encode('ascii','ignore')+"\n")
		f.write(datetime.datetime.today().strftime('%b-%d-%Y'))
		f.close()

	return

def getGoogleTrendsData(geoCode)
    pytrend = TrendReq(hl='en-US', tz=360)
    pytrend.build_payload(kw_list['flu'], cat=0, timeframe='today 1-m', geo=geoCode, gprop='')
    x = pytrend.interest_by_region(resolution='CITY')

    return x.to_dict()


