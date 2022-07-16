from global_hotkeys import *
import time

import play

isAlive = True

def kill():
	global isAlive
	isAlive = False

def reload():
	play.load("..\\celeste", "testNotes", "Result")
	print("done loading")

bindings = [
	[["right_shift"], reload, None],
    [["right_control"], play.play, None],
	[["escape"], kill, None]
]


if __name__ == "__main__":
	register_hotkeys(bindings)

	play.init()

	play.load("..\\celeste", "testNotes", "Result")

	start_checking_hotkeys()

	print("Keys:\nesc: kill this program\nright shift: reload tas file\nright control: play the tas file")

	while isAlive:
		time.sleep(0.1)