#game_stats.py
from settings import Settings
import pygame

class GameStats:
	"""Track statistics for Alien Invasion"""
	
	def __init__(self, ai_game):
		"""initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		#start Alien Invasion in an active state.
		self.game_active = True
		
	def reset_stats(self):
		"""initialize statistics than can change during the game"""
		self.ships_left = self.settings.ship_limit
		
		
