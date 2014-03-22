import datetime

from django.utils import timezone
from django.test import TestCase

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


