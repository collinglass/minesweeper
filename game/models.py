from django.db import models
#from matrix_field import MatrixField
from django.utils import timezone

# Create your models here.
class Game(models.Model):
    board = models.CharField(max_length=200)
    over = models.BooleanField()
    winner = models.BooleanField()
    counter = models.PositiveSmallIntegerField()
    start_date = models.DateTimeField('date started')
    end_date = models.DateTimeField('date ended')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)