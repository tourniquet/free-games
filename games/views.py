from django.shortcuts import render

from .models import Game, Genre, Platform


def index(request):
  games = Game.objects.all()
  genres = Genre.objects.all()
  context = {'games': games, "genres": genres}

  return render(request, 'games/index.html', context)


def by_genre(request, genre):
  games = Game.objects.filter(genres__title=genre)
  context = {"games": games}

  return render(request, 'games/index.html', context)


def by_platform(request, platform):
  games = Game.objects.filter(platform__title=platform)
  context = {'games': games}

  return render(request, 'games/index.html', context)
