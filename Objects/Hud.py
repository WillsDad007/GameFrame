from GameFrame import TextObject, Globals
import pygame

tutorial_text_1 = (
    "WELCOME, FACT CHECKER!\n"
    "\n"
    "Your mission: Stop misinformation from spreading!\n"
    "You'll investigate news articles and decide\n"
    "whether each one is FAKE or LEGIT.\n"
    "\n"
    "HOW TO SPOT FAKE NEWS:\n"
    "\n"
    "1. CHECK THE SOURCE\n"
    "Is the website trustworthy? Look for strange\n"
    "URLs, unfamiliar publishers or fake logos.\n"
    "Remember: A professional look proves nothing!\n"
    "\n"
    "2. QUESTION THE HEADLINE\n"
    "Does it sound shocking or too good to be true?\n"
    "Clickbait uses dramatic words to grab attention.\n"
    "Don't judge an article by its headline alone!\n"
    "\n"
    "3. INVESTIGATE THE EVIDENCE\n"
    "Are there facts, reliable sources or expert\n"
    "quotes? Can other trusted websites confirm it?\n"
    "Big claims need strong evidence!\n"
)

tutorial_text_2 = (
     "4. CHECK THE DETAILS\n"
        "Look at the author, publication date and images.\n"
        "Old stories can be shared as if they're new.\n"
        "Real images can also be used out of context!\n"
        "\n"
        "HOW TO PLAY:\n"
        "\n"
        "Read each article carefully and investigate\n"
        "the clues before making your decision.\n"
        "Choose FAKE if the information is misleading,\n"
        "or LEGIT if the claims are supported by facts.\n"
        "Earn points for correct answers and learn\n"
        "from the explanation after each decision.\n"
        "\n"
        "FINAL TIP:\n"
        "If you're unsure, don't guess or share it.\n"
        "Pause, investigate and verify the facts!\n"
        "\n"
        "READY TO BECOME A MISINFORMATION DETECTIVE?"
        "\n"
        "Press SPACE to start game."
)


class Tutorial_Title(TextObject): 
    def __init__(self, room, x, y, 
                 text='Tutorial', 
                 size=60,
                 font='Comic Sans MS', 
                 colour=(255, 255, 255), 
                 bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

        self.handle_key_events = True

    def key_pressed(self, key):
            if key[pygame.K_SPACE]:
                self.room.running = False

class Tutorial_Text_1(TextObject): 
    def __init__(self, room, x, y, 
                 text=tutorial_text_1, 
                 size=20,
                 font='Comic Sans MS', 
                 colour=(255, 255, 255), 
                 bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Tutorial_Text_2(TextObject): 
    def __init__(self, room, x, y, 
                 text=tutorial_text_2, 
                 size=20,
                 font='Comic Sans MS', 
                 colour=(255, 255, 255), 
                 bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

        