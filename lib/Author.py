from Article import Article

class Author:
    _all_authors = []

    def __init__(self, name):
        self._name = name
        self._articles = []
        Author._all_authors.append(self)

    @property
    def name(self):
        return self._name

    @property
    def articles(self):
        return self._articles

    def add_article(self, magazine, title):
        article = Article(self, magazine, title)
        self._articles.append(article)
        return article

    @property
    def magazines(self):
        return list(set(article.magazine for article in self.articles))

    def topic_areas(self):
        return list(set(magazine.category for magazine in self.magazines))

