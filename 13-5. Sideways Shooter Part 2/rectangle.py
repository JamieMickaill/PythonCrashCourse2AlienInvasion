#rectangle.py
import pygame
from settings import Settings

class Rectangle:
	def __init__ (self, ai_game):
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.screen_rect = ai_game.screen.get_rect()
		self.rect = pygame.Rect(1100,100,50,200)
		
		self.y = float(self.rect.y)
		
	def _draw_rect(self):
		pygame.draw.rect(self.screen, (0,0,0), self.rect)
		
	def update(self):
		"""move the rectangle to the up or down"""
	
		self.rect.y += (self.settings.rectangle_speed *
				self.settings.rectangle_direction)
				
	def check_edges(self):
		"""return True if alien is at the edge of screen"""
		screen_rect = self.screen.get_rect()
		if self.rect.bottom >= screen_rect.bottom or self.rect.top <= -1:
			return True
	
