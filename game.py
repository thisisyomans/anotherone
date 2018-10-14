import pygame, math, time, random, os, sys
from pygame.locals import *

#NOTE: alternative method for filepaths, meant to make packaging easier
#EXAMPLE: pygame.image.load(resource_path(os.path.join('resources', 'image.png')))
#EXAMPLE: pygame.mixer.Sound(resource_path(os.path.join('resources', 'sound.wav')))
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)

def main():
	#initialize game
	pygame.init()

	#screen details
	pygame.display.set_caption('RoboTirade')
	width, height = 640, 480
	screen = pygame.display.set_mode((width, height))
	
	#setting up fps
	frame_count = 0
	frame_rate = 0
	t0 = time.clock()

	#any needed vars, arrays, lists, etc
	keys = [False, False, False, False]

	#NOTE: image resources + small manipulations

	#NOTE: sound resources + small manipulations

	#NOTE: game itself???
	running = True #better than ust running a "while True:" loop, now we can check program state w/ a var
	exitcode = 0 #change num in game code and then call the next screen, exitcode will decide the next screen

	while running:
		
		eventlook = pygame.event.poll()
		
		if eventlook.type == pygame.QUIT():
			pygame.quit()
		if eventlook.type == pygame.KEYDOWN:
			if event.key == K_q:
                pygame.quit()
			


		frame_count += 1
        if frame_count % 500 == 0:
            t1 = time.clock()
            frame_rate = 500 / (t1-t0)
            t0 = t1
		
		pygame.display.flip()
	
	if exitcode == 0:

	if exitcode == 1:


main()