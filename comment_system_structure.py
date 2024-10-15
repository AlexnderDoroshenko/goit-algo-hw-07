class Comment:
    def __init__(self, text: str, author: str):
        """
        Initializes a comment.

        :param text: The text of the comment.
        :param author: The author of the comment.
        """
        self.text: str = text
        self.author: str = author
        self.replies: list[Comment] = []
        self.is_deleted: bool = False

    def add_reply(self, reply: 'Comment') -> None:
        """Adds a new reply to the comment."""
        self.replies.append(reply)

    def remove_reply(self) -> None:
        """Removes a reply from the comment."""
        if self.replies:
            self.text = "This comment has been deleted."
            self.is_deleted = True

    def display(self, indent: int = 0, replies_list: list = None) -> None:
        """Displays the comment and all its replies with indentation."""
        print('    ' * indent + f"{self.author}: {self.text}")
        replies = replies_list if replies_list else self.replies
        for reply in replies:
            reply.display(indent + 1)
            if reply.replies:
                self.display(indent, reply.replies)


# Test


def test_comment_system():
    root_comment = Comment("What a wonderful book!", "Bodhi")
    reply1 = Comment("The book is a total disappointment :(", "Andriy")
    reply2 = Comment("What is wonderful about it?", "Marina")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment(
        "It's not a book, just a pile of paper translated for nothing...", "Serhiy")
    reply1.add_reply(reply1_1)
    root_comment.display(4)

    reply1.remove_reply()
    root_comment.display(4)
    exp_comments = ("This comment has been deleted.",
                    "What is wonderful about it?",
                    "It's not a book, just a pile of paper translated for nothing...")
    assert root_comment.replies[0].text == exp_comments[0], \
        "Expected comments not matched"
    assert root_comment.replies[1].text == exp_comments[1], \
        "Expected comments not matched"
    assert root_comment.replies[0].replies[0].text == exp_comments[2], \
        "Expected comments not matched"
    print("The comments test passed")


test_comment_system()
