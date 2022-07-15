import json
from midiutil.MidiFile import MIDIFile

sourceFileName = "1B"
noteFileName = "testNotes"
outputFileName = "1B-TAM"


mf = MIDIFile(1)     # only 1 track
track = 0   # the only track

time = 0    # start at the beginning
mf.addTrackName(track, time, "Tool Assisted Music")
mf.addTempo(track, time, 3600)

# add some notes
channel = 0
volume = 100

rows = []

with open(sourceFileName + ".tas", 'r') as file:
    for line in file.readlines():
        line = line.strip()
        if line != "":
            if line[0].isnumeric():
                line = line.split(",")
                for i in range(int(line[0])):
                    rows.append(tuple(map(lambda x: x.strip(), line[1:])))

noteLookup = {}

with open(noteFileName+".json", 'r') as file:
    noteLookup = json.load(file)

counters = {}

for key in noteLookup.keys():
    counters[key] = 0

timeCounter=0
for row in rows:
    for key in counters.keys():
        if key in row:
            counters[key] += 1
        elif counters[key] > 0:
            print(f"Added note {noteLookup[key]} (key {key}) from {timeCounter-counters[key]}-{timeCounter-1}")
            mf.addNote(track, channel, noteLookup[key], timeCounter-counters[key], counters[key], volume)
            counters[key] = 0
    timeCounter += 1



with open(outputFileName + ".mid", 'wb') as outf:
    mf.writeFile(outf)