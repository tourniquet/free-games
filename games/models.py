from django.db import models


class Genre(models.Model):
  title = models.CharField(max_length=255, unique=True)

  class Meta:
    verbose_name_plural = 'genres'

  def __str__(self):
    return self.name


class Game(models.Model):
  title = models.CharField(max_length=255)
  urls = models.CharField(max_length=255)
  genres = models.ManyToManyField(Genre)
  created = models.DateTimeField(auto_now_add=True)
  expires = models.DateTimeField()
  image = models.ImageField(upload_to='images', null=True, blank=True)

  class Meta:
    verbose_name_plural = 'games'

  def __str__(self):
    return self.name
