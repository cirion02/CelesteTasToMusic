import json
from midiutil.MidiFile import MIDIFile

sourceFileName = "1A"
noteFileName = "testNotes"
outputFileName = "1A-ALT-TAM"


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
                rows.append([int(line[0])] + list(map(lambda x: x.strip(), line[1:])))

noteLookup = {}

with open(noteFileName+".json", 'r') as file:
    noteLookup = json.load(file)

timeCounter=0
for row in rows:
    for key in row[1:]:
        print(f"Added note {noteLookup[key]} (key {key}) from {timeCounter}-{timeCounter+row[0]}")
        mf.addNote(track, channel, noteLookup[key], timeCounter, row[0], volume)
    timeCounter += row[0]

with open(outputFileName + ".mid", 'wb') as outf:
    mf.writeFile(outf)