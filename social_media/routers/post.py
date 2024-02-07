from fastapi import APIRouter

from social_media.models.post import UserPost, UserPostIn

router = APIRouter()


post_table = {}


@router.post("/post", response_model=UserPost)
async def create_post(post: UserPostIn):
    data = post.model_dump()
    last_recorded_id = len(post_table)
    new_post = {**data, "id": last_recorded_id}
    post_table[last_recorded_id] = new_post
    return new_post


@router.get("/post", response_model=list[UserPost])
async def get_all_post():
    return list(post_table.values())
