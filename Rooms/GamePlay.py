from GameFrame import Level, Globals
import random
from Objects.News_Item import News_Item, Article_Title, Article_Author, Article_Date, Article_Source, Article_Text

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image
        self.set_background_image("news_background.png")

        self.articles = Globals.articles.copy()
        random.shuffle(self.articles)
        self.article_index = 0
        self.article = self.articles[self.article_index]

        # add roomobject title, author, date, source, text
        self.add_room_object(Article_Title(self, 30, 100, text=self.article.title))
        self.add_room_object(Article_Author(self, 915, 413))
        self.add_room_object(Article_Date(self, 915, 493))
        self.add_room_object(Article_Source(self, 915, 573))
        self.add_room_object(Article_Text(self, 30, 170))

        self.article_index += 1
        if self.article_index < len(self.articles):
            self.article = self.articles[self.article_index]
        else:
            # end of game, make it switch to new list later
            pass

        