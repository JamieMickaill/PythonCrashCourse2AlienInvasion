#alien invasion

import sys

import pygame

from ship2 import Ship
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
		
	def run_game(self):
		"""start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			
			
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
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right= True
		if event.key == pygame.K_LEFT:
			self.ship.moving_left= True
		if event.key == pygame.K_UP:
			self.ship.moving_up= True
		if event.key == pygame.K_DOWN:
			self.ship.moving_down= True
		elif event.key == pygame.K_q:
			sys.exit()

				
	def _check_events_KEYUP(self,event):
		"""check keydown events"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False
		if event.key == pygame.K_UP:
			self.ship.moving_up= False
		if event.key == pygame.K_DOWN:
			self.ship.moving_down= False
			
	def _update_screen(self):
		"""update the screen size"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		pygame.display.flip()
			
if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
	
	





