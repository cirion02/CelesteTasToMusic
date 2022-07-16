import create
import pygame

def play():
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy(): 
		pygame.time.Clock().tick(10)

def init():
	pygame.init()
	pygame.mixer.init()

def load(sourceFileName, noteFileName, outputFileName):
	create.main(sourceFileName, noteFileName, outputFileName, False, True)
	pygame.mixer.music.load(outputFileName + ".mid")

if __name__ == "__main__":
	sourceFileName, noteFileName, outputFileName = ("..\\celeste", "testNotes", "Result")

	init()
	load(sourceFileName, noteFileName, outputFileName)
	play()