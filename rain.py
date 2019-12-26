#rain.py

import pygame
from pygame.sprite import Sprite
from settings import Settings

class Rain(Sprite):
	"""A class to represent a single star in the sky"""
	
	def __init__ (self, ai_game):
		"""Initialize the alien and set its starting position."""
		super(). __init__()
		self.screen = ai_game.screen
		
		#load the rain image and set its rect attribute
		self.image = pygame.image.load('images/rain.png')
		self.rect = self.image.get_rect()
		self.settings = ai_game.settings
		
		#start each new raindrop at the top left, above the screen
		self.rect.x = 0
		self.rect.y = -100
		#store the rains position as a decimal value
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

#*********************************************************************8

	def update(self):
		"""move the rain down the screen"""
		#update the decimal position of the rain
		self.y += self.settings.rain_speed
		#updte the rect position
		self.rect.y = self.y

	def check_edges(self):
		"""return True if rain is at the edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom:
			return True

		
		#the rain class doesnt need a method for drawing it to the screen
		#instead we'll use a pygame group method that will draw all the elements


#determining how many aliens will fit in a row
#		available_space_x = settings.screen_width – (2 * alien_width)
# We also need to set the spacing between aliens; we’ll make it one alien width.
# 		number_aliens_x = available_space_x // (2 * alien_width)
