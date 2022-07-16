from global_hotkeys import *
import time
import threading

import play

isAlive = True

def kill():
	global isAlive
	isAlive = False

def reload():
	play.load("..\\celeste", "testNotes", "Result")
	print("done loading")

runThread = threading.Thread(target=play.play)

bindings = [
	[["right_shift"], reload, None],
    [["right_control"], runThread.run, None]
]


if __name__ == "__main__":
	register_hotkeys(bindings)

	play.init()

	play.load("..\\celeste", "testNotes", "Result")

	start_checking_hotkeys()

	print("Keys:\nright shift: reload tas file\nright control: play the tas file\nenter: stop playing sound")

	while isAlive:
		time.sleep(0.1)