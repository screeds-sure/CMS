# comment.py

class Comment:
    def __init__(self, comment_id, content, user):
        self.comment_id = comment_id
        self.content = content
        self.user = user

    def display_info(self):
        print(f"Comment ID: {self.comment_id}")
        print(f"Content: {self.content}")
        print(f"User: {self.user.display_info()}")
