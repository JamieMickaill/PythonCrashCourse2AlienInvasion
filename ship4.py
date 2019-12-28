#ship.py

import pygame
from settings import Settings

class Ship:
	"""a class to manage the ship"""
	
	def __init__(self, ai_game):
		"""initialize the ship and set its starting position"""
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		
		
		#load the ship image and get its rect.
		self.image = pygame.image.load('images/ship4.png')
		self.rect = self.image.get_rect()
		
		# Start each new ship at the middle of the right hand side of the screen. 
		self.rect.midleft = self.screen_rect.midleft
		
		#store a decimal value for the ship's horizontal position.
		self.x = float(self.rect.x)
		self.y = float(self.rect.y)
		
		#movement flag
		self.moving_up = False
		self.moving_down = False		
		
		
	def update(self):
		"""update the ships position based on movement flags"""
		#update the ships x value, not the rect.
		if self.moving_up and self.rect.top > 0:
			self.y -= self.settings.ship_speed
		if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
			self.y += self.settings.ship_speed
			
		#update rect object from self
		self.rect.x = self.x
		self.rect.y = self.y
	
	def blitme(self):
		"""Draw the ship at its current location."""
		self.screen.blit(self.image,self.rect)
		
		
	def center_ship(self):
		self.rect.midleft = self.screen_rect.midleft
		self.x = float(self.rect.x)
