import csv
import pygmaps

lat = []
long = []

with open('/Users/madurasenadeera/github/BCC-water-fountain-locations/data/20181101open-datapark-bubblers2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for value in csv_reader:
        lat.append(value[9])
        long.append(value[10])

# print lat
# print long


mymap = pygmaps.gmap(39.0194, 125.7381, 8)
mymap.add_point(39.0194, 125.7381, title="test")
#mymap.add_point(37.5665, 126.978)
mymap.draw('./mymap.html')
