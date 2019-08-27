# -*- coding: utf-8 -*-

# Import Main class
from transporthours.main import Main

# Create an instance
myTh = Main()

# Define some OSM tags to convert
# We use a simple dict
myTags = {
	"type": "route",
	"route": "bus",
	"name": "Ligne 42",
	"opening_hours": "Mo-Fr 05:00-22:00",
	"interval": "00:30",
	"interval:conditional": "00:10 @ (Mo-Fr 07:00-09:30, 16:30-19:00)"
}

# Ask to convert your OSM tags into a parsed object
myInterpretedHours = myTh.tagsToHoursObject(myTags)

print()
print("==== Interpreted tags ====")
print(myInterpretedHours)
print()

# Ask to convert in a format for GTFS export
myGtfsHours = myTh.tagsToGtfs(myTags)

print()
print("==== GTFS interpretation ====")
print(myGtfsHours)
print()
