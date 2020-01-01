#target_practice

import sys
from time import sleep
import pygame


from ship4 import Ship
from bullet4 import Bullet
from alien4 import Alien
from settings import Settings
from game_stats import GameStats
from rectangle import Rectangle
from playbutton import Button



class AlienInvasion:
	"""Overall class to manage game assets and behaviour"""
	
	def __init__ (self):
		"""initialize the game, and create game resources."""
		pygame.init()
		self.settings = Settings()
	
		
		self.screen = pygame.display.set_mode(
		(self.settings.screen_width, self.settings.screen_height))
		self.stats = GameStats(self)
		pygame.display.set_caption("Alien Invasion")
		
		self.ship = Ship(self)
		self.bullets = pygame.sprite.Group()
		self.rect = Rectangle(self)
		self.play_button = Button(self, "Play")
		
	def run_game(self):
		"""start the main loop for the game."""
		while True:
			self._check_events()
			if self.stats.game_active:
				
				self.ship.update()
				self._update_bullets()
				self._update_rectangle()
				
			self._update_screen()
						
	def _check_events(self):
		#watch for keyboard and mouse events
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				sys.exit()
			elif event.type == pygame.KEYDOWN:				
				self._check_events_KEYDOWN(event)
			elif event.type == pygame.KEYUP:
				self._check_events_KEYUP(event)
			elif event.type == pygame.MOUSEBUTTONDOWN:
				mouse_pos = pygame.mouse.get_pos()
				self._check_play_button(mouse_pos)


	def _start_game(self):
		"""start game with fresh stats"""
		self.stats.reset_stats()
		self.stats.game_active = True
		self.bullets.empty()
		self.ship.center_ship()
		pygame.mouse.set_visible(False)
		self.settings.bullets_available = 3

				
				
	def _check_play_button(self, mouse_pos):
		"""start a new game when the player clicks play"""
		button_clicked = self.play_button.rect.collidepoint(mouse_pos)
		if button_clicked and not self.stats.game_active:
			self.settings.initialize_dynamic_settings()
			self._start_game()
			
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
			if self.settings.bullets_available >= 1:
				new_bullet = Bullet(self)
				self.bullets.add(new_bullet)
				self.settings.bullets_available -=1
			else:
				self.stats.game_active=False
				print("GAME OVER")
			
	def _update_bullets(self):
		"""update position of bullets and get rid of old bullets."""
		#update bullet positions
		self.bullets.update()
		#get rid of bullets when they have dissapeared.
		for bullet in self.bullets.copy():
			if bullet.rect.right >= 1200:
				self.bullets.remove(bullet)
#		print(len(self.bullets))	- to see if they are being deleted

	def _check_fleet_edges(self):
		"""respond appropriately if any aliens have reached an edge."""
		if self.rect.check_edges():
			self._change_rectangle_direction()
			
			
	def _change_rectangle_direction(self):
		"""drop the entire fleet and change the fleets direction"""
		self.settings.rectangle_direction *= -1

	def _update_rectangle(self):
		self.rect.update()
		self._check_fleet_edges()
		self._check_bullet_rectangle_collisions()
		
	def _check_bullet_rectangle_collisions(self):
		#check for any bullets that have hit aliens
		#if so get rid of the bullet and the alien
		collision = pygame.sprite.spritecollideany(self.rect, self.bullets)
		if collision:
			print("nice!")
			self.settings.bullets_available = 3
			self.settings.increase_speed()

		
						
	def _update_screen(self):
		"""update the screen size"""
		self.screen.fill(self.settings.bg_color)
		self.ship.blitme()
		self.rect._draw_rect()
		for bullet in self.bullets.sprites():
			bullet.draw_bullet()
		if not self.stats.game_active:
			self.play_button.draw_button()
			pygame.mouse.set_visible(True)
			
		
				
		pygame.display.flip()
			
if __name__ == '__main__':
	#make a game instance, and run the game.
	ai = AlienInvasion()
	ai.run_game()
	
	





