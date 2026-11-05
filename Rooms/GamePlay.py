from GameFrame import Level
from Objects.News_Item import News_Item, Article_Title, Article_Author, Article_Date, Article_Source, Article_Text

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image
        self.set_background_image("news_background.png")

        # add roomobject news item
        #self.add_room_object(News_Item(self, 30, 180))

        # add roomobject title
        self.add_room_object(Article_Title(self, 30, 100))

        # add roomobject author
        self.add_room_object(Article_Author(self, 915, 413))

        # add roomobject date
        self.add_room_object(Article_Date(self, 915, 493))

        # add roomobject source
        self.add_room_object(Article_Source(self, 915, 573))

        # add roomobject text
        self.add_room_object(Article_Text(self, 30, 170))
        