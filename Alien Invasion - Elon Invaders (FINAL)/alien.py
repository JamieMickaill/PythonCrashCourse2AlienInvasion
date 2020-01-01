#alien.py
import pygame
from pygame.sprite import Sprite
from settings import Settings

class Alien(Sprite):
	"""A class to represent a singe alien in the fleet"""
	
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
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height * 2
		
		#store the alien's axact horizontal position
		#so we can track the aliens speed
		self.x = float(self.rect.x)
		
		#the alien class doesnt need a method for drawing it to the screen
		#instead we'll use a pygame group method that will draw all the elements
	def update(self):
		"""move the alien to the right or left"""
		self.x += (self.settings.alien_speed *
				self.settings.fleet_direction)
		self.rect.x = self.x
		
	def check_edges(self):
		"""return True if alien is at the edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.right >= screen_rect.right or self.rect.left <= 0:
			return True
	

#determining how many aliens will fit in a row
#		available_space_x = settings.screen_width – (2 * alien_width)
# We also need to set the spacing between aliens; we’ll make it one alien width.
# 		number_aliens_x = available_space_x // (2 * alien_width)
