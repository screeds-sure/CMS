# article.py

class Article:
    def __init__(self, article_id, title, content, author):
        self.article_id = article_id
        self.title = title
        self.content = content
        self.author = author

    def display_info(self):
        print(f"Article ID: {self.article_id}")
        print(f"Title: {self.title}")
        print(f"Content: {self.content}")
        print(f"Author: {self.author.display_info()}")
