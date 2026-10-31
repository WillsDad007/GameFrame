from GameFrame import Level,Globals
from Objects.Title import Title

class WelcomeScreen(Level):
    """
    Game Welcome Screen
    """
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image
        self.set_background_image("background.png")

        # add title to room object
        self.add_room_object(Title(self, 240, 200))
