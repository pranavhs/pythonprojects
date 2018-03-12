# 
# Example file for parsing and processing JSON
#
import urllib.request 
import json

def printResults(data):
  # Use the json module to load the string data into a dictionary
  theJSON = json.loads(data)
  
  # now we can access the contents of the JSON like any other Python object
  if "title" in theJSON["metadata"]:
    print(theJSON["metadata"]["title"])
  
  # output the number of events, plus the magnitude and each event name  
  count = theJSON["metadata"]["count"]
  print(str(count) + " events recorded")

  # for each event, print the place where it occurred
  greatFour = 0
  for i in theJSON["features"]:
    if i["properties"]["mag"] >= 4.0:
      print("\n----------")
      print("Magnitude: " + str(i["properties"]["mag"]) + "Location: " + i["properties"]["place"])
      greatFour=greatFour+1
      print("----------\n")
  print("Number of Magnitude 4.0 or larger Earthquakes in the past 24 hours:" + str(greatFour))

  # print the events that only have a magnitude greater than 4
  #done above
      
  # print only the events where at least 1 person reported feeling something
  felt = 0
  for j in theJSON["features"]:
    if not(j["properties"]["felt"] == None):
      if j["properties"]["felt"] >= 1:
        print("\n----------")
        print("Magnitude: " + str(j["properties"]["mag"]) + "\nLocation: " + j["properties"]["place"] + "\nNumber of people who felt it: " + str(j["properties"]["felt"]))
        felt=felt+1
        print("----------\n")
  print("Number of felt Earthquakes in the past 24 hours:" + str(felt))
  
def main():
  # define a variable to hold the source URL
  # In this case we'll use the free data feed from the USGS
  # This feed lists all earthquakes for the last day larger than Mag 2.5
  urlData = "http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

  # Open the URL and read the data
  webUrl = urllib.request.urlopen(urlData)
  print ("result code: " + str(webUrl.getcode()))
  if (webUrl.getcode()==200):
    data = webUrl.read()
    printResults(data)
  else:
    print("error")


if __name__ == "__main__":
  main()
