#alien.py
import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
	"""A class to represent a singe alien in the fleet"""
	
	def __init__ (self, ai_game):
		"""Initialize the alien and set its starting position."""
		super(). __init__()
		self.screen = ai_game.screen
		
		
		#load the alien image and set its rect attribute
		self.image = pygame.image.load('images/alien.png')
		self.rect = self.image.get_rect()
		
		#start each new alien near the top left of the screen
		#we add a space to the left of it that’s equal to the alien’s width 
		#and a space above it equal to its height 
		self.rect.x = self.rect.width
		self.rect.y = self.rect.height
		
		#store the alien's axact horizontal position
		#so we can track the aliens speed
		self.x = float(self.rect.x)
		
		#the alien class doesnt need a method for drawing it to the screen
		#instead we'll use a pygame group method that will draw all the elements


#determining how many aliens will fit in a row
#		available_space_x = settings.screen_width – (2 * alien_width)
# We also need to set the spacing between aliens; we’ll make it one alien width.
# 		number_aliens_x = available_space_x // (2 * alien_width)
