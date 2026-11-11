from GameFrame import TextObject, Globals
import pygame

tutorial_text_1 = (
    "WELCOME, FACT CHECKER!\n"
    "\n"
    "You've just joined the newsroom!\n"
    "Your boss has a problem: misinformation is\n"
    "spreading, and the public needs your help.\n"
    "Your mission is to investigate 18 articles\n"
    "and decide which are FAKE or LEGIT.\n"
    "\n"
    "HOW TO SPOT FAKE NEWS:\n"
    "\n"
    "1. CHECK THE SOURCE\n"
    "Is the publisher trustworthy? Look for\n"
    "unfamiliar sources or suspicious details.\n"
    "A professional appearance proves nothing!\n"
    "\n"
    "2. QUESTION THE HEADLINE\n"
    "Does it sound shocking or too good to be true?\n"
    "Clickbait uses dramatic words for attention.\n"
    "But strange claims can still be real!\n"
    "\n"
    "3. INVESTIGATE THE EVIDENCE\n"
    "Are experts, studies or statistics provided?\n"
    "Can other reliable sources confirm the story?\n"
    "Big claims need strong evidence!"
)


tutorial_text_2 = (
    "4. CHECK THE DETAILS\n"
    "Look at the author and publication date.\n"
    "Old stories can be shared as if they're new.\n"
    "AI can also create convincing fake content!\n"
    "\n"
    "HOW TO PLAY:\n"
    "\n"
    "Read each article and investigate the clues.\n"
    "Press F if you believe the article is FAKE.\n"
    "Press R if you believe the article is REAL.\n"
    "\n"
    "Correct answers earn points, while incorrect\n"
    "answers reduce your score.\n"
    "Check the grey notification box after answering\n"
    "to discover whether you were correct and why.\n"
    "Press SPACE to move to the next article.\n"
    "\n"
    "FINAL TIP:\n"
    "Don't trust everything you read, even if it\n"
    "looks professional. Investigate and verify!\n"
    "\n"
    "Your boss is counting on you to stop fake news.\n"
    "Don't let the newsroom down!\n"
    "\n"
    "READY TO START FACT-CHECKING?\n"
    "Press SPACE to begin!"
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
                 size=17,
                 font='Comic Sans MS', 
                 colour=(255, 255, 255), 
                 bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

class Tutorial_Text_2(TextObject): 
    def __init__(self, room, x, y, 
                 text=tutorial_text_2, 
                 size=17,
                 font='Comic Sans MS', 
                 colour=(255, 255, 255), 
                 bold=False): 
        TextObject.__init__(self, room, x, y, text, size, font, colour, bold)

        