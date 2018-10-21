import pygame, math, time, random, os, sys, ezpygame
from pygame.locals import *

#NOTE: alternative method for filepaths, meant to make packaging easier
#EXAMPLE: pygame.image.load(resource_path(os.path.join('resources', 'image.png')))
#EXAMPLE: pygame.mixer.Sound(resource_path(os.path.join('resources', 'sound.wav')))
def resource_path(relative):
	if hasattr(sys, "_MEIPASS"):
		return os.path.join(sys._MEIPASS, relative)
	return os.path.join(relative)

width, height = 640, 480
keys = [False, False, False, False]
exitcode = 0
running = 0

#NOTE: image resources

#NOTE: audio resources


class Menu(ezpygame.Scene):
	title = ' - Main Menu'

	def __init__(self, size):
        super().__init__()

	def on_enter(self, previous_scene):
        super().on_enter(previous_scene)
        self.previous_scene = None
	
	def on_exit(self, next_scene):
		super.on_exit(next_scene)
		self.next_scene = game_screen

    #self.application.change_scene(self.previous_scene)
	#self.application.change_scene(self.next_scene)

class Game(ezpygame.Scene):
	title = ""
	update_rate = 60
	running = 1

	def __init__(self, size):
        super().__init__()

	def on_enter(self, previous_scene):
        super().on_enter(previous_scene)
        self.previous_scene = main_menu
	
	def on_exit(self, next_scene):
		super.on_exit(next_scene)
		if exitcode == 0:
			self.next_scene = lose_screen
		else:
			self.next_scene = win_screen	

class Lose(ezpygame.Scene): #exitcode of 0
	title = ' - You Lose!'
	running = 0

	def __init__(self, size):
        super().__init__()

	def on_enter(self, previous_scene):
        super().on_enter(previous_scene)
        self.previous_scene = game_screen
	
	def on_exit(self, next_scene):
		super.on_exit(next_scene)
		self.next_scene = main_menu

class Win(ezpygame.Scene): #exitcode of 1
	title = ' - You Win!'
	running = 0

	def __init__(self, size):
        super().__init__()

	def on_enter(self, previous_scene):
        super().on_enter(previous_scene)
        self.previous_scene = game_screen
	
	def on_exit(self, next_scene):
		super.on_exit(next_scene)
		self.next_scene = main_menu

app = ezpygame.Application(
	title = '',
	resolution = (width, height),
	update_rate =  30
)

main_menu = Menu()
game_screen = Game()
lose_screen = Lose()
win_screen = Win()
app.run(main_menu)