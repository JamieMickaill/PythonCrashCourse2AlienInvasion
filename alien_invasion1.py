#Alien_invasion1

import pygame
import sys

class AlienInvasion():
	"""general class for alien invasion game"""
	def __init__(self):
		pygame.init()
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0,0,230)
		self.screen = pygame.display.set_mode(
		(self.screen_width, self.screen_height))
		pygame.display.set_caption("Alien Invasion")
	
	
		

	def run_game(self):
		while True:
			self.screen.fill(self.bg_color)
			pygame.display.flip()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()
	
	
if __name__ == '__main__':
	ai = AlienInvasion()
	ai.run_game()
	
