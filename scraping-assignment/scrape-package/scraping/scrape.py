import pandas as pd
import requests

url = 'http://events.uoit.ca/events-feed.php?start=2017-12-31&end=2018-02-11&_=1517198573279'

resp = requests.get(url)
while resp.status_code != 200:
	resp = requests.get(url)
	
#print(resp.json())

headers = ['id','title','start','end','tags','className','allDay']

data = resp.json()
data = pd.DataFrame(data, columns=headers)

data.to_csv('uoit-events.csv', index=False)

