#game_stats.py
from settings import Settings
import pygame
import json

class GameStats:
	"""Track statistics for Alien Invasion"""
	
	def __init__(self, ai_game):
		"""initialize statistics"""
		self.settings = ai_game.settings
		self.reset_stats()
		#start Alien Invasion in an inactive state.
		self.game_active = False
		#highscore should never be reset
		
		filename = 'high_score.json'
		try:
			with open(filename) as f:
				self.high_score = json.load(f)
		except json.decoder.JSONDecodeError:
			self.high_score = 0		
		except FileNotFoundError:
			self.high_score = 0
		

		
	def reset_stats(self):
		"""initialize statistics than can change during the game"""
		self.ships_left = self.settings.ship_limit
		self.score = 0
		self.level = 1
		
		
