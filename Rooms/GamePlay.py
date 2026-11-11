from GameFrame import Level, Globals, TextObject
import random
from Objects.News_Item import News_Item, Article_Title, Article_Author, Article_Date, Article_Source, Article_Text, Progress, Score
import pygame
import time
from Objects.News_Item import Score
from Objects.Notification import Notification

class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)

        # set background image and sounds
        self.set_background_image("news_background.png")

        self.background_music = self.load_sound("Italian_Mom.ogg")
        self.background_music.set_volume(0.5)
        self.background_music.play(loops=-1)
        self.good_sound = self.load_sound("good.ogg")
        self.bad_sound = self.load_sound("bad.ogg")
        self.click_sound = self.load_sound("click3.ogg")
        self.congrats_sound = self.load_sound("roblox-congrats.mp3")

        # add score
        self.score = Score(self,
                           915, 115,
                           f"Score: {str(Globals.SCORE)}")
        self.add_room_object(self.score)

        # add room object progress
        self.progress_object = Progress(self, 355, 650)
        self.add_room_object(self.progress_object)

        self.articles = Globals.articles.copy()
        random.shuffle(self.articles)
        self.article_index = 0
        self.article = self.articles[self.article_index]

        # answer for real/fake and correct or not
        self.answer_submitted = False
        self.player_answer = None

        # add notification text
        self.notification_object = Notification(
            self, 915, 170
        )
        self.add_room_object(self.notification_object)


        # add roomobject title, author, date, source, text
        self.title_object = Article_Title(
            self, 30, 110, text=self.article.title
        )

        self.author_object = Article_Author(
            self, 915, 413, text=self.article.author
           )

        self.date_object = Article_Date(
            self, 915, 493, text=self.article.date
           )
        
        self.source_object = Article_Source(
            self, 915, 573, text=self.article.source
            )

        self.text_object = Article_Text(
            self, 30, 170, text=self.article.text
           )
        
        self.add_room_object(self.title_object)
        self.add_room_object(self.author_object)
        self.add_room_object(self.date_object)
        self.add_room_object(self.source_object)
        self.add_room_object(self.text_object)
        self.add_room_object(News_Item(self, 30, 170))
        

    def switch_article(self):
        if self.answer_submitted == True:
            self.article_index += 1

            if self.article_index < len(self.articles):
                self.article = self.articles[self.article_index]

                # progress update
                self.progress_object.text = f"Progress: {self.article_index + 1}/18"
                self.progress_object.update_text()

                # set new background
                if self.article_index == 9:
                    self.set_background_image("news_background.png")
                elif self.article_index == 1 or self.article_index == 10:
                    self.set_background_image("news_background2.png")
                elif self.article_index == 2 or self.article_index == 11:
                    self.set_background_image("news_background3.png")
                elif self.article_index == 3 or self.article_index == 12:
                    self.set_background_image("news_background4.png")
                elif self.article_index == 4 or self.article_index == 13:
                    self.set_background_image("news_background5.png")
                elif self.article_index == 5 or self.article_index == 14:
                    self.set_background_image("news_background6.png")
                elif self.article_index == 6 or self.article_index == 15:
                    self.set_background_image("news_background7.png")
                elif self.article_index == 7 or self.article_index == 16:
                    self.set_background_image("news_background8.png")
                elif self.article_index == 8 or self.article_index == 17:
                    self.set_background_image("news_background9.png")

                # update article
                self.title_object.text = self.article.title
                self.author_object.text = self.article.author
                self.date_object.text = self.article.date
                self.source_object.text = self.article.source
                self.text_object.text = self.article.text
        
                self.title_object.update_text()
                self.author_object.update_text()
                self.date_object.update_text()
                self.source_object.update_text()
                self.text_object.update_text()

                # clear notification
                self.notification_object.text = ""
                self.notification_object.update_text()

                # reset answer state
                self.answer_submitted = False
                self.player_answer = None
            else:
                self.congrats_sound.play()
                time.sleep(2)
                Globals.exiting = True
                quit()
        else:
            pass

    def show_notification(self):
        if self.player_answer == self.article.is_fake:
            self.notification_object.text = ("Correct!\n"
            f"{self.article.explanation}")
            self.good_sound.play()
        elif self.player_answer != self.article.is_fake:
            self.notification_object.text = ("Incorect :(\n"
            f"{self.article.explanation}")
            self.bad_sound.play()
        self.notification_object.update_text()


        
