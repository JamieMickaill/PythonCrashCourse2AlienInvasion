#alien invasion

import sys

import pygame

from ship import Ship
from stars import Star
from bullet import Bullet
from alien import Alien
from settings import Settings
from rain import Rain
from random import randint
x = randint(1,6)

	

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
		self.stars = pygame.sprite.Group()
		self._create_stars()
		self.rains = pygame.sprite.Group()
		self._create_rains()
		
	def run_game(self):
		"""start the main loop for the game."""
		while True:
			self._check_events()
			self._update_screen()
			self.ship.update()
			self._update_bullets()
			self._update_aliens()
			self._update_rains()
			
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
		alien_width, alien_height = alien.rect.size
		available_space_x = self.settings.screen_width - (1 * alien_width)
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
		alien.x = alien_width + 2 * alien_width * alien_number
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
			alien.rect.y += self.settings.fleet_drop_speed
		self.settings.fleet_direction *= -1


	def _create_stars(self):
		#make a star and find the number of stars in a row
		star = Star(self)
		star_width, star_height = star.rect.size
		
		#determine the amount of stars in a row
		available_space_x = self.settings.screen_width 
		number_stars_x = available_space_x // ( 1 * star_width)
		#determine the number of rows
		available_space_y = self.settings.screen_height
		number_rows = available_space_y // (1 * star_height)
		
		for row_number in range(number_rows):
			for star_number in range(number_stars_x):
				self._create_star(star_number, row_number)
				
				
		
					
	def _create_star(self, star_number, row_number):
		"""create a star and place it in the row"""
		star = Star(self)
		star_width, star_height = star.rect.size
		star.x =  + (star_width * ten.roll_die()) * star_number
		star.rect.x = star.x
		star.rect.y = (star.rect.height * ten.roll_die()) * row_number
		self.stars.add(star)
				
#***************************************************** RAIN


	def _create_rains(self):
		#make a raindrop and find the number of rains in a row
		rain = Rain(self)
		rain_width, rain_height = rain.rect.size
		
		#determine the amount of stars in a row
		available_space_x = self.settings.screen_width 
		number_rains_x = available_space_x // rain_width
		#determine the number of rows
		available_space_y = self.settings.screen_height
		number_rows = available_space_y //(2 * rain_height)
		
		for row_number in range(number_rows):
			for rain_number in range(number_rains_x):
				self._create_rain(rain_number, row_number)
				
				
		
					
	def _create_rain(self, rain_number, row_number):
		"""create a rain and place it in the row"""
		rain = Rain(self)
		rain_width, rain_height = rain.rect.size
		rain.x = (rain_width * hunit.roll_die()) * rain_number
		rain.y = rain.rect.height * row_number
		rain.rect.x = rain.x
		rain.rect.y = rain.y
		self.rains.add(rain)
		
	def _update_rains(self):
		"""update position of bullets and get rid of old bullets."""
		#update rain positions
		self.rains.update()
		#get rid of raindrops when they have dissapeared.
		for rain in self.rains.copy():
			if rain.rect.bottom >= 850:
				self.rains.remove(rain)
				if len(self.rains) <= self.settings.rains_allowed:
					self._create_rains()		


#*****************************************************
	
	def _update_screen(self):
		"""update the screen size"""
		self.screen.fill(self.settings.bg_color)
		self.stars.draw(self.screen)
		self.rains.draw(self.screen)
		self.ship.blitme()
		self.aliens.draw(self.screen)

		
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
			
		pygame.display.flip()
		
		
class Die():
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		return(randint(1,self.sides))

ten = Die(10)
hunit = Die(30)
			
if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
	
	





