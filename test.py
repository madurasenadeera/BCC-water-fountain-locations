import csv
import pygmaps

lat = []
long = []

with open('/Users/madurasenadeera/github/BCC-water-fountain-locations/data/20181101open-datapark-bubblers2.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    for value in csv_reader:
        lat.append(value[9])
        long.append(value[10])

print lat
print long
