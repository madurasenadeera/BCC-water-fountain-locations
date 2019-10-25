import csv
import pygmaps
import webbrowser

lat = []
lon = []

with open('/Users/madurasenadeera/github/BCC-water-fountain-locations/data/20181101open-datapark-bubblers2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    next(csv_reader)
    for value in csv_reader:
        lat.append(value[9])
        lon.append(value[10])


mymap = pygmaps.gmap(-27.470030, 153.022980, 15)

for lati in lat:
    for long in lon:
        latitude = float(lati)
        longitude = float(long)
        #print(latitude, longitude)
        mymap.add_point(latitude, longitude)

mymap.draw('./mymap.html')

# open file in browser
url = "file:///Users/madurasenadeera/github/BCC-water-fountain-locations/mymap.html"
webbrowser.open(url, new=2)
