#alien invasion

import sys

import pygame

from ship4 import Ship
from bullet4 import Bullet
from settings import Settings

class AlienInvasion:
	"""Overall class to manage game assets and behaviour"""
	
	def __init__ (self):
		"""initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()
		
		self.screen = pygame.display.set_mode(
		(self.settings.screen_width, self.settings.screen_height))
		
		pygame.display.set_caption("Alien Invasion")
		
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		
	def run_game(self):
		"""start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			self._update_bullets()
			
	def _check_events(self):
		#watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:				
				self._check_events_KEYDOWN(event)
			elif event.type == pygame.KEYUP:
				self._check_events_KEYUP(event)
			
	def _check_events_KEYDOWN(self,event):
		"""check keydown events"""
		if event.key == pygame.K_UP:
			self.ship.moving_up= True
		if event.key == pygame.K_DOWN:
			self.ship.moving_down= True
		if event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			
			sys.exit()

				
	def _check_events_KEYUP(self,event):
		"""check keydown events"""
		if event.key == pygame.K_UP:
			self.ship.moving_up= False
		if event.key == pygame.K_DOWN:
			self.ship.moving_down= False
			
	def _fire_bullet(self):
		"""Create a new bullet and add it to the bullets group"""
		if len(self.bullets) < self.settings.bullets_allowed:
			new_bullet = Bullet(self)
			self.bullets.add(new_bullet)
			
	def _update_bullets(self):
		"""update position of bullets and get rid of old bullets."""
		#update bullet positions
		self.bullets.update()
		#get rid of bullets when they have dissapeared.
		for bullet in self.bullets.copy():
			if bullet.rect.right >= 1200:
				self.bullets.remove(bullet)
#		print(len(self.bullets))	- to see if they are being deleted


			
	def _update_screen(self):
		"""update the screen size"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		pygame.display.flip()
			
if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
	
	





