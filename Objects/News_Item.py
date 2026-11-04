from GameFrame import TextObject, Globals, RoomObject
import pygame
import random

class News_Item(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # get news item
        item = random.choice(Globals.articles)
        print(item.title)