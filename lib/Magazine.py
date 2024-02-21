from Article import Article

class Magazine:
    _all_magazines = []

    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine._all_magazines.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        self._category = value

    @classmethod
    def all(cls):
        return cls._all_magazines

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls._all_magazines:
            if magazine.name == name:
                return magazine
        return None

    def contributors(self):
        authors = set(article.author for article in Article._all_articles if article.magazine == self)
        return list(authors)

    def article_titles(self):
        return [article.title for article in Article._all_articles if article.magazine == self]

    def contributing_authors(self):
        author_articles = {}
        for article in Article._all_articles:
            if article.magazine == self:
                author_articles[article.author] = author_articles.get(article.author, 0) + 1
        return [author for author, count in author_articles.items() if count > 2]

