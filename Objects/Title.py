from GameFrame import RoomObject
import pygame
from GameFrame import Globals

class Title(RoomObject):
    """
    Object for displaying title
    """
    def __init__(self, room, x, y):
        RoomObject.__init__(self, room, x, y)

        # set image
        image = self.load_image("Title.png")
        self.set_image(image,800,350)

        # register key events
        self.handle_key_events = True

    def key_pressed(self, key):
        """
        If Space pressed, game starts, if T pressed, opens tutorial
        """
        if key[pygame.K_SPACE]:
            self.room.running = False
            Globals.next_level = 2
        elif key[pygame.K_t]:
            self.room.running = False
            Globals.next_level = 1