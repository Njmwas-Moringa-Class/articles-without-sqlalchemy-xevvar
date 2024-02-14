from Author import Author
from Magazine import Magazine

class Article:

    all_articles = []

    def __init__(self, author, magazine, title ) -> None:
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.add_to_all_articles(self)

    def get_title(self):
        return self._title

    def author(self):
        return self._author

    def magazine(self):
        return self._magazine
    
    @classmethod
    def add_to_all_articles(cls, article):
        cls.all_articles.append(article)

    @classmethod
    def show_all_articles(cls):
        return [article._title for article in cls.all_articles]
