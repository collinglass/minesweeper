from django.db import models
from django.utils import timezone

# Create your models here.
class Board(models.Model):
    width = models.PositiveSmallIntegerField()
    height = models.PositiveSmallIntegerField()
    numberOfMines = models.PositiveSmallIntegerField()

class Tile(models.Model):
	board = models.ForeignKey(Board)
	mine = models.BooleanField()
	revealed = models.BooleanField()
	marked = models.BooleanField()
	value = models.PositiveSmallIntegerField()
	x = models.PositiveSmallIntegerField()
	y = models.PositiveSmallIntegerField()

	def reveal(self):
		self.revealed = True
		return self.mine == True

	def mark(self):
		self.marked = True
		return self.mine == True

	def evaluate(self, value):
		self.value = value