class IdNotFoundError(Exception):
    """Raised when there is no post with provided id"""

    pass


def get_post_by_id(posts, id):
    for post in posts:
        if id == post['id']:
            return post
    raise IdNotFoundError
