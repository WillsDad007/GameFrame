from GameFrame import TextObject, Globals, RoomObject
import pygame
import random

class News_Item(RoomObject): 
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("blank.png")
        self.set_image(image,50,50)
        

        # get news item
        item = random.choice(Globals.articles)
        print(item.title)

class Article_Title(TextObject): 
    def __init__(self, room, x, y, 
            text='title', 
            size=50,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Author(TextObject): 
    def __init__(self, room, x, y, 
            text='author', 
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Date(TextObject): 
    def __init__(self, room, x, y, 
            text='date', 
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Source(TextObject): 
    def __init__(self, room, x, y, 
            text='source', 
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Text(TextObject): 
    def __init__(self, room, x, y, 
            text='text', 
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Explanation(TextObject): 
    def __init__(self, room, x, y, 
            text='explain', 
            size=30,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
