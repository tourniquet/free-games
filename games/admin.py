from django.contrib import admin

from .models import Game, Genre, Platform


admin.site.register(Genre)
admin.site.register(Platform)


@admin.register(Game)
class EntryAdmin(admin.ModelAdmin):
  list_display = ('title', 'created', 'expires',)
