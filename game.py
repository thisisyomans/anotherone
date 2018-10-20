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
	#maybe not for the menu screen and game screens, cause conflicting keys/actions, but probably for the 2 end screens

def main():
	#initialize game
	pygame.init()

	#screen details
	pygame.display.set_caption('')
	width, height = 640, 480
	screen = pygame.display.set_mode((width, height))

	#setting up fps
	frame_count = 0
	frame_rate = 0
	t0 = time.clock()

	#any needed vars, arrays, lists, etc
	restart = False
	keys = [False, False, False, False]
	running = 2 #better than just running a "while True:" loop, now we can check program state w/ a var
	exitcode = 0 #change num in game code, set running to False, when running is set to False, while loop breaks, and game looks for next screen based on exitcode

	#NOTE: possible restart function
	#def restart_game():
		#if(restart == True):
			#restart = False
			#change running state to switch scenes

	#event system
	def event_system():
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				pygame.quit()
			
			if event.type == pygame.KEYDOWN:
				if event.key == K_q:
					pygame.quit()

				if event.key == K_r and running == 3:
					restart = True
					restart_game()

				if event.key == K_w:
					keys[0] = True
				if event.key == K_a:
					keys[1] = True
				if event.key == K_s:
					keys[2] = True
				if event.key == K_d:
					keys[3] = True

			if event.type == pygame.KEYUP:

				if event.key == K_w:
					keys[0] = False
				if event.key == K_a:
					keys[1] = False
				if event.key == K_s:
					keys[2] = False
				if event.key == K_d:
					keys[3] = False

	#NOTE: image resources + small manipulations

	#NOTE: sound resources + small manipulations

	#NOTE: game itself
	while running == 1 and restart == False: #NOTE: menu
		#probably a clickable sprite button on screen for starting the game
		#pygame.display.flip(), pretty sure I don't need it for now, but you never know
		event_system() #I don't think I need the key system here, gonna have to check the logic

	while running == 2 and restart == False: #NOTE: game screen
		frame_count += 1
		if frame_count % 500 == 0:
			t1 = time.clock()
			frame_rate = 500 / (t1-t0)
			t0 = t1

		screen.fill((255, 255, 255))
		
		my_font = pygame.font.Font(resource_path(os.path.join('resources', 'freesansbold.ttf')), 24)
		the_text = my_font.render("Frame = {0},  rate = {1:.2f} fps"
		.format(frame_count, frame_rate), True, (0,0,0))
		screen.blit(the_text, (10, 10))
		
		pygame.display.flip()
		event_system()

	if exitcode == 0 and running == 3 and restart == False: #NOTE: losing end screen
		#pygame.display.flip(), pretty sure I don't need it for now, but you never know
		event_system()

	if exitcode == 1 and running == 3 and restart == False: #NOTE: winning end screen
		#pygame.display.flip(), pretty sure I don't need it for now, but you never know
		event_system()

main()
