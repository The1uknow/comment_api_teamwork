from db import get_db
from db.models import Comment, User, UserPost


"""
добавление
получение коммента по айди юзера (вернет все)
получение коммента по айди поста (вернет все)
изменение коммента
удаление коммента
"""


def create_comment_db(user_id: int, post_id: int, text: str):
    db = next(get_db())

    # проверка что юзер и пост существуют
    if not db.query(User).filter_by(id=user_id).first():
        return False
    if not db.query(UserPost).filter_by(id=post_id).first():
        return False

    new_comment = Comment(user_id=user_id, post_id=post_id, text=text)
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return True


def get_comments_by_user_db(user_id: int):
    db = next(get_db())

    return db.query(Comment).filter_by(user_id=user_id).first()


def get_comments_by_post_db(post_id: int):
    db = next(get_db())

    return db.query(Comment).filter_by(post_id=post_id).first()


def update_comment_db(comment_id: int, new_text: str):
    db = next(get_db())

    comment = db.query(Comment).filter_by(id=comment_id).first()
    if not comment:
        return False
    comment.text = new_text
    db.commit()
    db.refresh(comment)
    return True


def delete_comment_db(comment_id: int):
    db = next(get_db())

    comment = db.query(Comment).filter_by(id=comment_id).first()
    if not comment:
        return False
    db.delete(comment)
    db.commit()
    return True