from django.contrib import admin
from game.models import Board, Tile

class TileInline(admin.TabularInline):
    model = Tile

class BoardAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Width', {'fields': ['width']}),
        ('Height', {'fields': ['height']}),
    ]
    inlines = [TileInline]

admin.site.register(Board, BoardAdmin)