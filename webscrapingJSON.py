import requests
url="https://analytics.usa.gov/data/live/browsers.json"
r=requests.get(url)
#print(r.json()['totals']['browser']['Nintendo 3DS Browser'])
print("Number of people visiting a US government website RIGHT NOW!")
print(r.json()['totals']['visits'])
