from GameFrame import RoomObject
import pygame
from GameFrame import Globals
import json
from Objects.Articles import Article


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
        
        self.load_articles()

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

    def load_articles(self):

        with open("Objects/Articles.json", "r") as file:
            data = json.load(file)

        for article_data in data:
            article = Article(
            article_data["title"],
            article_data["author"],
            article_data["date"],
            article_data["source"],
            article_data["text"],
            article_data["is_fake"],
            article_data["explanation"]
            )
            Globals.articles.append(article)

