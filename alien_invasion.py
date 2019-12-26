#alien invasion

import sys

import pygame

from ship import Ship
from bullet import Bullet
from alien import Alien
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
		self.aliens = pygame.sprite.Group()
		self._create_fleet()
		
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
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right= True
		if event.key == pygame.K_LEFT:
			self.ship.moving_left= True
		if event.key == pygame.K_SPACE:
			self._fire_bullet()
		elif event.key == pygame.K_q:
			
			sys.exit()

				
	def _check_events_KEYUP(self,event):
		"""check keydown events"""
		if event.key == pygame.K_RIGHT:
			self.ship.moving_right = False
		if event.key == pygame.K_LEFT:
			self.ship.moving_left = False
			
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
			if bullet.rect.bottom <= 0:
				self.bullets.remove(bullet)
#		print(len(self.bullets))	- to see if they are being deleted

	def _create_fleet(self):
		"""create the fleet of aliens."""
		#make an alien and find the number of aliens in a row
		#spacing between each alien is equal to one alien width
		alien = Alien(self)
		alien_width = alien.rect.width
		available_space_x = self.settings.screen_width - (1 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)
				
		#create the first row of aliens.
		for alien_number in range(number_aliens_x):
			self._create_alien(alien_number)
			
			
	def _create_alien(self, alien_number):
		#create an alien and place it in the row.
		alien = Alien(self)
		alien_width = alien.rect.width
		alien.x = alien_width + 2 * alien_width * alien_number
		alien.rect.x = alien.x
		self.aliens.add(alien)
			
	def _update_screen(self):
		"""update the screen size"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		self.aliens.draw(self.screen)
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
			
		pygame.display.flip()
			
if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
	
	





