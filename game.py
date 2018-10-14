import pygame, math, time, random, os, sys
from pygame.locals import *

#NOTE: alternative method for filepaths, meant to make packaging easier
#EXAMPLE: pygame.image.load(resource_path(os.path.join('resources', 'image.png')))
#EXAMPLE: pygame.mixer.Sound(resource_path(os.path.join('resources', 'sound.wav')))
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)

#NOTE: image resources + small manipulations

#NOTE: sound resources + small manipulations

#NOTE: game itself???
running = 1
exitcode = 0 #change this in game code and then call the next screen, exitcode will decide the next screen