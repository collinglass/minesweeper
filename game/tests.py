import datetime

from django.utils import timezone
from django.test import TestCase
from django.core.urlresolvers import reverse
from django.test.client import Client as RequestClient

from game.models import Board, Tile
from game import views

class BoardCreationTests(TestCase):

	def test_correct_width_on_board_creation(self):
		"""
		board was created with width
		"""
		newboard = Board.objects.create(width=10, 
			height=10)
		self.assertEqual(newboard.width, 10)

	def test_correct_height_on_board_creation(self):
		"""
		board was created with proper height
		"""
		newboard = Board.objects.create(width=10, 
			height=10)
		self.assertEqual(newboard.height, 10)

class TileCreationTests(TestCase):

	def test_correct_x_on_tile_creation(self):
		"""
		tile was created with proper x
		"""
		newboard = Board.objects.create(width=10, 
			height=10)
		tile = Tile.objects.create(board=newboard, mine=True, revealed=False, marked=False, value=0, x=5, y=5)
		self.assertEqual(tile.x, 5)

	def test_correct_y_on_tile_creation(self):
		"""
		tile was created with proper y
		"""
		newboard = Board.objects.create(width=10, 
			height=10)
		tile = Tile.objects.create(board=newboard, mine=True, revealed=False, marked=False, value=0, x=5, y=5)
		self.assertEqual(tile.y, 5)

class TileUpdateTests(TestCase):

	def test_reveal_tile(self):
		"""
		tile was revealed correctly
		"""
		newboard = Board.objects.create(width=10, 
			height=10)
		tile = Tile.objects.create(board=newboard, mine=True, revealed=False, marked=False, value=0, x=5, y=5)
		self.assertEqual(tile.revealed, False)
		tile.revealed = True
		tile.save()
		self.assertEqual(tile.revealed, True)


	def test_mark_tile(self):
		"""
		tile was marked correctly
		"""
		newboard = Board.objects.create(width=10, 
			height=10)
		tile = Tile.objects.create(board=newboard, mine=True, revealed=False, marked=False, value=0, x=5, y=5)
		self.assertEqual(tile.marked, False)
		tile.marked = True
		tile.save()
		self.assertEqual(tile.marked, True)

class GameViewCreationTests(TestCase):
	def test_new_game_board_not_null(self):
		"""
		New game, board not null.
		"""
		# Get new game
		response = self.client.get(reverse('game:index'))
		# Assert proper response
		self.assertEqual(response.status_code, 200)
		# Assert Board is defined
		self.assertNotEqual(response.context['board'], None)

	def test_new_game_board_type_board(self):
		"""
		New game, board is of type board.
		"""
		# Get new game
		response = self.client.get(reverse('game:index'))
		# Assert proper response
		self.assertEqual(response.status_code, 200)
		# Assert board is of indeed a Board
		self.assertEqual(type(response.context['board']), Board)

	def test_new_game_tile_not_null(self):
		"""
		New game, tile not null.
		"""
		# Get new game
		response = self.client.get(reverse('game:index'))
		# Assert proper response
		self.assertEqual(response.status_code, 200)
		# Assert tiles is defined
		self.assertNotEqual(response.context['tiles'], None)

	def test_new_game_tile_type_tile(self):
		"""
		New game, tile is of type tile.
		"""
		# Get new game
		response = self.client.get(reverse('game:index'))
		# Assert proper response
		self.assertEqual(response.status_code, 200)
		# Get tiles
		tiles = response.context['tiles']
		# Assert first tile is indeed a tile
		self.assertEqual(type(tiles[0]), Tile)

class GameViewPlayTests(TestCase):
	def test_game_post_request(self):
		"""
		Test In game post request.
		"""
		# Get new game
		response = self.client.get(reverse('game:index'))
		# Assert proper response
		self.assertEqual(response.status_code, 200)
		# Get board
		board = response.context['board']
		# Get Tiles
		tiles = response.context['tiles']
		# Make post
		response = self.client.post('/game/'+`board.id`+'/', {'x': 1,
			'y': 2,'shift': 'off' })
		# Assert proper response
		self.assertEqual(response.status_code, 200)

	def test_game_reveal_tile(self):
		"""
		Tile should update as revealed.
		"""
		# Get new game
		response = self.client.get(reverse('game:index'))
		# Assert proper response
		self.assertEqual(response.status_code, 200)
		# Get board
		board = response.context['board']
		# Get Tiles
		tiles = response.context['tiles']
		# Assert tile is not revealed yet
		self.assertEqual(tiles[0].revealed, False)
		# Post click to reveal tile
		response = self.client.post('/game/'+`board.id`+'/', {'x': 0,
			'y': 0,'shift': 'off' })
		# Get tiles again
		tiles = response.context['tiles']
		# Assert tile is now revealed
		self.assertEqual(tiles[0].revealed, True)

	def test_game_mark_tile(self):
		"""
		Tile should update as marked.
		"""
		# Get new game
		response = self.client.get(reverse('game:index'))
		# Assert proper response
		self.assertEqual(response.status_code, 200)
		# Get board
		board = response.context['board']
		# Get Tiles
		tiles = response.context['tiles']
		# Assert tile is not yet marked
		self.assertEqual(tiles[0].marked, False)
		# Post shift click to mark tile
		response = self.client.post('/game/'+`board.id`+'/', {'x': 0,
			'y': 0,'shift': 'on' })
		# Get Tiles
		tiles = response.context['tiles']
		# Assert Tile is now marked
		self.assertEqual(tiles[0].marked, True)







