#settings.py

class Settings:
	"""A class to store all settings for alien invasion."""
	
	def __init__(self):
		"""initialize the game's static settings."""
		#screen settings
		self.screen_width = 1200
		self.screen_height = 800
		self.bg_color = (0,0,0)
		
		#ship settings
		self.ship_limit = 3

		
		#bullet settings
		self.bullet_width = 3
		self.bullet_height = 15
		self.bullet_color = (0,255,6)
		self.bullets_allowed = 3
		self.bullets_available = 3
		
		#rectangle settings

		self.rectangle_width = 10
		self.rectangle_height = 50
		self.rectangle_color = (60,60,60)
		self.rectangle_direction = 1		
		
		
		#alien settings
		self.fleet_drop_speed = 10

		#rain settings
		self.rain_speed = 5
		self.rains_allowed = 100
		
		#how quickly the game speeds up
		self.speedup_scale = 1.1
		self.score_scale = 1.5
		self.initialize_dynamic_settings()
		
		self.display_difficulty_options = False
		
	def initialize_dynamic_settings(self):
		"""initialize the settings that change throughout the game"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		self.rectangle_speed = 1
		self.alien_points = 100
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1

	def initialize_easy_settings(self):
		"""initialize the settings that change throughout the game"""
		self.ship_speed = 1.5
		self.bullet_speed = 3.0
		self.alien_speed = 1.0
		self.rectangle_speed = 1
		self.alien_points = 100
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		
	def initialize_medium_settings(self):
		"""initialize the settings that change throughout the game"""
		self.ship_speed = 2.5
		self.bullet_speed = 3.0
		self.alien_speed = 2.0
		self.rectangle_speed = 1
		self.alien_points = 100
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
		
	def initialize_hard_settings(self):
		"""initialize the settings that change throughout the game"""
		self.ship_speed = 3.5
		self.bullet_speed = 1.0
		self.alien_speed = 3.0
		self.rectangle_speed = 1
		self.alien_points = 100
		#fleet_direction of 1 represents right; -1 represents left
		self.fleet_direction = 1
				

		
	def increase_speed(self):
		"""increase speed settings"""
		self.ship_speed *= self.speedup_scale
		self.bullet_speed *= self.speedup_scale
		self.alien_speed *= self.speedup_scale
		self.rectangle_speed *= self.speedup_scale
		self.alien_points = int(self.alien_points * self.score_scale)

		
