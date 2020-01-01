#bullet.py
import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
	"""Create a bullet object at the shiip's current position."""
	def __init__ (self,ai_game):
		super().__init__()
		self.screen = ai_game.screen
		self.settings = ai_game.settings
		self.color = self.settings.bullet_color
	
		#Create a bullet rect as (0,0) then set correct position
		self.rect = pygame.Rect(0,0, self.settings.bullet_width,
			self.settings.bullet_height)
		self.rect.midtop = ai_game.ship.rect.midright
	
		#store the bullets position as a decimal value
		self.y = float(self.rect.y)
		self.x = float(self.rect.x)

	def update(self):
		"""move the bullet up the screen"""
		#update the decimal position of the bullet
		self.x += self.settings.bullet_speed
		#updte the rect position
		self.rect.x = self.x
		
	def draw_bullet(self):
		"""draw the bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)
