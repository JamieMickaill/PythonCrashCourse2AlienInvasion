#alien4.py

import pygame
from settings import Settings
from pygame.sprite import Sprite

class Alien(Sprite):
	"""a class to represent a single alien in the fleet"""
	def __init__ (self, ai_game):
		"""Initialize the alien and set its starting position."""
		super(). __init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		
		#load the alien image and set its rect attribute
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()
		
		#start each new alien near the top left of the screen
		#we add a space to the left of it that’s equal to the alien’s width 
		#and a space above it equal to its height 
		self.rect.x = 800
		self.rect.y = self.rect.height
		
		
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)

	def update(self):
		"""move the alien to the right or left"""
		self.rect.y += (self.settings.alien_speed *
				self.settings.fleet_direction)
		
	def check_edges(self):
		"""return True if alien is at the edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= -1:
			return True
	
