# transporthours.main

## Main
```python
Main(self)
```

Main class of the library.
It contains all main functions which can help managing public transport hours.

### tagsToGtfs
```python
Main.tagsToGtfs(self, tags)
```

Convert OpenStreetMap tags into a GTFS-like format (list of dict having format { eachWeekDay: True/False, start_time: string, end_time: string, headway: int }.
Parsed tags are : interval=\*, opening_hours=\* and interval:conditional=\*

__param tags (dict): OpenStreetMap tags__

__return dict[]: list of dictionaries, each one representing a line of GTFS hours CSV file__


### tagsToHoursObject
```python
Main.tagsToHoursObject(self, tags)
```

Converts OpenStreetMap tags into a ready-to-use object representing the hours of the public transport line.
Parsed tags are : interval=\*, opening_hours=\* and interval:conditional=\*

__param tags (dict): The list of tags from OpenStreetMap__

__return dict: The hours of the line, with structure { opens: object in format given by `OpeningHoursParser.gettable()`, defaultInterval: minutes (int), otherIntervals: interval rules object, otherIntervalsByDays: list of interval by days (structure: { days: string[], intervals: { hoursRange: interval } }), allComputedIntervals: same as otherIntervalsByDays but taking also default interval and opening_hours }. Each field can also have value "unset" if no tag is defined, or "invalid" if tag can't be read.__


### intervalConditionalStringToObject
```python
Main.intervalConditionalStringToObject(self, intervalConditional)
```

Reads an interval:conditional=* tag from OpenStreetMap, and converts it into a JS object.

__param intervalConditional (string): The {@link https://wiki.openstreetmap.org/wiki/Key:interval|interval:conditional} tag__

__return (dict[]): A list of rules, each having structure { interval: minutes (int), applies: {@link `gettable`|opening hours table} }__


### intervalStringToMinutes
```python
Main.intervalStringToMinutes(self, interval)
```

Converts an interval=* string into an amount of minutes

>>> intervalStringToMinutes("00:10")
10

# transporthours.openinghoursparser

## OpeningHoursParser
```python
OpeningHoursParser(self, value)
```

OpeningHoursParser handles parsing of opening_hours=* tag.
It only supports basic version of the tag, as we don't need full implementation for public transport hours.

### getTable
```python
OpeningHoursParser.getTable(self)
```

Get the parsed value as a table
__return (dict): The hours, as { day: [ hours ] }__


