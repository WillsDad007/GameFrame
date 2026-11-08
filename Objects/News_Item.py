from GameFrame import TextObject, Globals, RoomObject
import pygame
import random
from Objects import Articles

class News_Item(RoomObject):
    """
    Class to register real/fake key event
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)
        image = self.load_image("blank.png")
        self.set_image(image,50,50)

        # register key events
        self.handle_key_events = True

    def key_pressed(self, key):
        """
        If R pressed, registers as real, and if F pressed, registers as fake, if space pressed, next
        """
        if self.room.answer_submitted:
            if key[pygame.K_SPACE]:
                self.room.switch_article()
                

        elif key[pygame.K_f]:
            player_answer = True
            self.room.answer_submitted = True
            self.room.show_notification()

        elif key[pygame.K_r]:
            player_answer = False
            self.room.answer_submitted = True
            self.room.show_notification()

        else:
            return
        
        if player_answer == self.room.article.is_fake:
            self.room.score.update_score(10)
            print("correct")

        else:
            print("incorrect")
            self.room.score.update_score(-5)
        self.room.player_answer = player_answer

class Article_Title(TextObject): 
    def __init__(self, room, x, y,
            text="", 
            size=50,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Author(TextObject): 
    def __init__(self, room, x, y, 
            text="", 
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Date(TextObject): 
    def __init__(self, room, x, y, 
            text="", 
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Source(TextObject): 
    def __init__(self, room, x, y, 
            text="",
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Text(TextObject): 
    def __init__(self, room, x, y, 
            text="", 
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Article_Explanation(TextObject): 
    def __init__(self, room, x, y, 
            text="",
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Progress(TextObject): 
    def __init__(self, room, x, y, 
            text="Progress: 1/9",
            size=20,
            font='Comic Sans MS', 
            colour=(0, 0, 0), 
            bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Score(TextObject):
    def __init__(self, room, x:int, y:int, text=None):
        TextObject.__init__(self, room, x, y, text)

        # set values         
        self.size = 20
        self.font = 'Comic Sans MS'
        self.colour = (0,0,0)
        self.bold = False
        self.update_text()

    def update_score(self, change):
        Globals.SCORE += change
        self.text = str(Globals.SCORE)
        self.update_text()
