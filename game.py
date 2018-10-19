import pygame, math, time, random, os, sys
from pygame.locals import *

#NOTE: alternative method for filepaths, meant to make packaging easier
#EXAMPLE: pygame.image.load(resource_path(os.path.join('resources', 'image.png')))
#EXAMPLE: pygame.mixer.Sound(resource_path(os.path.join('resources', 'sound.wav')))
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)

#MAJOR NOTE: maybe create function outside of main for event handling that is called inside each of the running states rather than writing the entire loop itself

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

	#NOTE: game itself
	running = 1 #better than just running a "while True:" loop, now we can check program state w/ a var
	exitcode = 0 #change num in game code, set running to False, when running is set to False, while loop breaks, and game looks for next screen based on exitcode

	while running == 1: #NOTE: menu

		eventlook = pygame.event.poll()
		
		if eventlook.type == pygame.QUIT():
			pygame.quit()
		
		if eventlook.type == pygame.KEYDOWN:
			if eventlook.key == K_q:
				pygame.quit()

		if eventlook.type == pygame.KEYUP:

	while running == 2: #NOTE: game screen
		
		eventlook = pygame.event.poll()
		
		if eventlook.type == pygame.QUIT():
			pygame.quit()
		
		if eventlook.type == pygame.KEYDOWN:
			if eventlook.key == K_q:
				pygame.quit()

			if eventlook.key == K_w:
				keys[0] = True
			if eventlook.key == K_a:
				keys[1] = True
			if eventlook.key == K_s:
				keys[2] = True
			if eventlook.key == K_d:
				keys[3] = True

		if eventlook.type == pygame.KEYUP:

		frame_count += 1
		if frame_count % 500 == 0:
			t1 = time.clock()
			frame_rate = 500 / (t1-t0)
			t0 = t1
		
		pygame.display.flip()
	
	if exitcode == 0 and running == 3: #NOTE: losing end screen
		
		eventlook = pygame.event.poll()
		
		if eventlook.type == pygame.QUIT():
			pygame.quit()
		
		if eventlook.type == pygame.KEYDOWN:
			if eventlook.key == K_q:
				pygame.quit()
			if eventlook.key == K_r:

		if eventlook.type == pygame.KEYUP:

	if exitcode == 1 and running == 3: #NOTE: winning end screen

		eventlook = pygame.event.poll()
		
		if eventlook.type == pygame.QUIT():
			pygame.quit()
		
		if eventlook.type == pygame.KEYDOWN:
			if eventlook.key == K_q:
				pygame.quit()
			if eventlook.key == K_r:

		if eventlook.type == pygame.KEYUP:

main()
