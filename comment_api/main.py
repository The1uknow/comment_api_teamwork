from fastapi import APIRouter
from pydantic import BaseModel
from db.comment_service import (
    create_comment_db,
    get_comments_by_user_db,
    get_comments_by_post_db,
    update_comment_db,
    delete_comment_db,
)

"""
- create_comment(user_id, post_id, text)
- get_comments_by_user(user_id)
- get_comments_by_post(post_id)
- update_comment(comment_id, text)
- delete_comment(comment_id)
"""

comment_router = APIRouter(prefix="/comment", tags=["Comment API"])

# пайдантик схемы для автоматической валидации
class CommentCreate(BaseModel):
    user_id: int
    post_id: int
    text: str


class CommentUpdate(BaseModel):
    comment_id: int
    new_text: str


# можете использовать мои функции как хелпер ответы либо прописать свои в эндпоинте как на уроке
def if_work(data: dict) -> dict:
    return {"status": 1, "data": data}

def if_error(message="error"):
    return {"status": 0, "message": message}



# тут пишет максим
@comment_router.post("/create_comment")
async def create_comment_api(comment: CommentCreate):
    try:
        create = create_comment_db(
            user_id=comment.user_id,
            post_id=comment.post_id,
            text=comment.text
        )
        if create:
            return if_work({"message": "комментарий создан"})
        return if_error("не удалось создать комментарий")
    except Exception:
        return if_error("ошибка при создании комментария")



# тут пишет андрей
@comment_router.get("/get_comments_by_user")






@comment_router.get("/get_comments_by_post")






# тут пишет сардор
@comment_router.put("/update_comment")
async def update_comment_api(comment_id: int, new_text: str):
    try:
        updated = update_comment_db(comment_id=comment_id, new_text=new_text)
        if updated:
            return if_work({"message": "комментарий обновлен"})
        return if_error("комментарий не найден")
    except Exception:
        return if_error("не удалось обновить комментарий")

# тут пишет мухсин
@comment_router.delete("/delete_comment")
async def delete_comment_api(comment_id: int):
    try:
        delete = delete_comment_db(comment_id=comment_id)
        if delete:
            return if_work({"message": "комментарий удален"})
        return if_error("комментарий не найден")
    except Exception:
        return if_error("не удалост удалить комментарий")
