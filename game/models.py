from django.db import models
from django.utils import timezone
from random import randrange

# Create your models here.
class Board(models.Model):
	width = models.PositiveSmallIntegerField()
	height = models.PositiveSmallIntegerField()

	# Make new Board
	def newBoard(self):
		try:
			# Board id
			board_id = self.id
			# Make array for tiles
			tiles = []
			# Create tiles
			for y in range(0, self.width):
				for x in range(0, self.height):
					# 10% will be mines
					if randrange(9) < 1:
						tiles.append(Tile.objects.create(board=self, mine=True, revealed=False, marked=False, value=0, x=x, y=y))
					# 90% will be empty
					else:
						tiles.append(Tile.objects.create(board=self, mine=False, revealed=False, marked=False, value=0, x=x, y=y))
			self.addValue(tiles)
		# Handle Exception
		except Exception as inst:
			print inst
		# Return new board and tiles
		return tiles

	# Add value to board tiles
	def addValue(self, tiles):
		try:
			# Update tile value if adjacent to mine
			for tile in tiles:
				position = (tile.y*10) + tile.x
				# Check left right
				if tile.x != 0:
					if tiles[position - 1].mine == True:
						tile.value += 1
				if tile.x != 9:
					if tiles[position + 1].mine == True:
						tile.value += 1
				# Check top left, center, right
				if tile.y != 0:
					if tiles[position - 10].mine == True:
						tile.value += 1
					if tile.x != 9:
						if tiles[position - 9].mine == True:
							tile.value += 1
					if tile.x != 0:
						if tiles[position - 11].mine == True:
							tile.value += 1
				# Check bottom left, center, right
				if tile.y != 9:
					if tiles[position + 10].mine == True:
						tile.value += 1
					if tile.x != 0:
						if tiles[position + 9].mine == True:
							tile.value += 1
					if tile.x != 9:
						if tiles[position + 11].mine == True:
							tile.value += 1
				tile.save()
		except Exception as inst:
			print inst

class Tile(models.Model):
	board = models.ForeignKey(Board)
	mine = models.BooleanField()
	revealed = models.BooleanField()
	marked = models.BooleanField()
	value = models.PositiveSmallIntegerField()
	x = models.PositiveSmallIntegerField()
	y = models.PositiveSmallIntegerField()

	# Mark tile
	def mark(self):
		try:
			# Mark tile
			self.marked = True
			self.save()
		# Handle exception
		except Exception as inst:
			print inst



