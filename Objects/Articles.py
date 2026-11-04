class Article:
    def __init__(self, title, author, date, source, text, is_fake: bool, explanation):
        self.title = title 
        self.author = author 
        self.date = date
        self.source = source
        self.text = text
        self.is_fake = is_fake
        self.explanation = explanation
