Requirements:
Python 3.10

Packages:
	pip install MIDIUtil			(for creation)

	pip install pygame				(for playback)

	pip install pypiwin32			(for shortcuts)
	pip install global-hotkeys -U	(for shortcuts)

Usage:
Put this folder in you celeste folder. It will always read the celeste.tas file in your celeste folder
				TODO: Add custom file usage

Navigate to the this folder in your terminal   (should be something like C:\Program Files (x86)\Steam\steamapps\common\Celeste\CelesteTasToMusic)

commands:
	python create.py
		Turns your celeste.tas file into a midi
	
	python play.py
		Turns your celeste.tas file into a midi and plays it

	python shortcuts.py
		Opens a window where you can start playback with hotkeys (can be used to roughly sync with ingame tas)

changing notes:
	you can modify testNotes.json to change which key plays which note. Change the number to the number you want. Use this chart to go from key to number https://www.inspiredacoustics.com/en/MIDI_note_numbers_and_center_frequencies

NOTES:
	Repeat, Load and other lines that start with anything but a number are ignored
	The exception is ***, using play and shortcuts the midi will start at the latest breakpoint