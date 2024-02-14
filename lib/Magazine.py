from Article import Article
from Author import Author

class Magazine:
    all_magazines = []

    def __init__(self, name, category) -> None:
        self.name = name
        self.category = category

        Magazine.add_to_all(self)

    def get_name(self):
        return self.name  
    
    def get_category(self):
        return self.category
    
    @classmethod
    def add_to_all(cls, magazine):
        cls.all_magazines.append(magazine)

    @classmethod
    def show_all_magazines(cls):
        print([magazine.name for magazine in cls.all_magazines])

    def contributors(self):
        return list(set(article.author() for article in Article.all_articles if article.magazine() == self))

    @classmethod
    def find_by_name(cls, name):
        for magazine in cls.all_magazines:
            if magazine.name() == name:
                return magazine
        return None  

    @classmethod
    def article_titles(cls, magazine_name):
        magazine = cls.find_by_name(magazine_name)
        if magazine:
            return [article.title() for article in Article.all_articles if article.magazine() == magazine]
        else:
            return []

    def contributing_authors(self):
        contributing_authors = []
        for author in Author.all_authors:
            articles_count = sum(1 for article in author.articles() if article.magazine() == self)
            if articles_count > 2:
                contributing_authors.append(author)
        return contributing_authors  
    