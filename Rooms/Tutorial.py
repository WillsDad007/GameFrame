from GameFrame import Level, Globals, RoomObject
from Objects.Hud import Tutorial_Title, Tutorial_Text_1, Tutorial_Text_2
import pygame

class Tutorial(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        title = Tutorial_Title(self, 0, 20)
        title.x = 640 - title.width / 2
        self.add_room_object(title)

        tutorial_1 = Tutorial_Text_1(self, 100, 150)
        self.add_room_object(tutorial_1)

        tutorial_2 = Tutorial_Text_2(self, 650, 150)
        self.add_room_object(tutorial_2)
        
        # set background image
        self.set_background_image("background.png")

