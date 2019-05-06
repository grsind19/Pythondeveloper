import urllib.request
import json
def printResut(data):
  theJSON = json.loads(data)
  print(theJSON)
  if "title" in  theJSON['metadata']:
    print(theJSON['metadata']['title'])

  count = theJSON['metadata']['count']

  print(str(count) + " events recorded")

def main():
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5"
  webUrl = urllib.request.urlopen(urlData)
  print("result code "+str(webUrl.getcode()))

  if webUrl.getcode() == 200:
    data = webUrl.read()
    printResut(data)
  else:
    print("Received error data")


if __name__ == "__main__":
    main()