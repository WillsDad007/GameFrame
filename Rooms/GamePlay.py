from GameFrame import Level
from Objects.News_Item import News_Item

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image
        self.set_background_image("news_background.png")

        # add roomobject title
        self.add_room_object(News_Item(self, 100, 100))