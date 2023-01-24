from django.db import models


class Genre(models.Model):
  title = models.CharField(max_length=255, unique=True)

  class Meta:
    verbose_name_plural = 'genres'

  def __str__(self):
    return self.title


class Platform(models.Model):
  title = models.CharField(max_length=100, unique=True)

  class Meta:
    verbose_name_plural = 'platforms'

  def __str__(self):
    return self.title


class Game(models.Model):
  title = models.CharField(max_length=255)
  url = models.CharField(max_length=255)
  genres = models.ManyToManyField(Genre)
  platform = models.ManyToManyField(Platform)
  created = models.DateTimeField(auto_now_add=True)
  expires = models.DateTimeField()
  image = models.ImageField(upload_to='images', null=True, blank=True)

  class Meta:
    verbose_name_plural = 'games'

  def __str__(self):
    return self.title
