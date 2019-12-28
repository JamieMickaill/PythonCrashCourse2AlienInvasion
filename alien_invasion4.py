#alien invasion

import sys

import pygame

from ship4 import Ship
from bullet4 import Bullet
from settings import Settings
from alien4 import Alien

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
			self._update_aliens()
			
			
			
			
			
			
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
		self._check_bullet_alien_collisions()
		#get rid of bullets when they have dissapeared.
		for bullet in self.bullets.copy():
			if bullet.rect.right >= 1200:
				self.bullets.remove(bullet)
#		print(len(self.bullets))	- to see if they are being deleted

	def _check_bullet_alien_collisions(self):
		collisions = pygame.sprite.groupcollide(
			self.bullets, self.aliens, True, True)
		if not self.aliens:
			#destroy exiting bullets and create new fleet
			self.bullets.empty()
			self._create_fleet()
		


	def _create_fleet(self):
		"""create the fleet of aliens."""
		#make an alien and find the number of aliens in a row
		#spacing between each alien is equal to one alien width
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (5 * alien_width)
		number_aliens_x = available_space_x // (2 * alien_width)
		
		#determine the number of rows of aliens that fit on the screen
		ship_height = self.ship.rect.height
		available_space_y = (self.settings.screen_height -
								(2 * alien_height) - ship_height)
		number_rows = available_space_y // (2 * alien_height)
						
		#create the full fleet of aliens.
		for row_number in range(number_rows):
			for alien_number in range(number_aliens_x):
				self._create_alien(alien_number, row_number)
			
			
			
	def _create_alien(self, alien_number, row_number):
		#create an alien and place it in the row.
		alien = Alien(self)
		alien_width, alien_height = alien.rect.size
		alien.x = (6 * alien_width) + (2 * alien_width * alien_number)
		alien.rect.x = alien.x
		alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
		self.aliens.add(alien)
		

	def _update_aliens(self):
		"""Check if the fleet is at the edge then
		update the positions of all the aliens in the fleet."""
		self._check_fleet_edges()
		self.aliens.update()

	def _check_fleet_edges(self):
		"""respond appropriately if any aliens have reached an edge."""
		for alien in self.aliens.sprites():
			if alien.check_edges():
				self._change_fleet_direction()
				break
				
	def _change_fleet_direction(self):
		"""drop the entire fleet and change the fleets direction"""
		for alien in self.aliens.sprites():
			alien.rect.x -= self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1
			
			
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
	
	





