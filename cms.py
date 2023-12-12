# cms.py

from user import User
from article import Article
from comment import Comment

# Create users
user1 = User(1, "Alice", "alice@example.com")
user2 = User(2, "Bob", "bob@example.com")

# Create articles
article1 = Article(101, "Introduction to Python", "Python is a versatile programming language.", user1)
article2 = Article(102, "Python Advanced Topics", "Exploring advanced features of Python.", user2)

# Create comments
comment1 = Comment(1001, "Great article!", user1)
comment2 = Comment(1002, "I learned a lot.", user2)

# Display information
print("User Information:")
user1.display_info()
print()
user2.display_info()

print("\nArticle Information:")
article1.display_info()
print()
article2.display_info()

print("\nComment Information:")
comment1.display_info()
print()
comment2.display_info()
