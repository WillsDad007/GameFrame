from GameFrame import RoomObject, TextObject, Globals
import pygame

class Notification(TextObject):
    def __init__(self, room, x, y,
        text="Placeholder text", 
        size=20,
        font='Comic Sans MS', 
        colour=(0, 0, 0), 
        bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)
        # control when popup appears, manage message displayed, handle interactions
        #1004, 200