from pydantic import BaseModel, ConfigDict


class UserPostIn(BaseModel):
    body: str


class UserPost(UserPostIn):
    model_config = ConfigDict(from_attibutes=True)  # to enable orm mode

    id: int


class CommentIn(BaseModel):
    body: str
    post_id: int


class Comment(CommentIn):
    model_config = ConfigDict(from_attibutes=True)  # to enable orm mode

    id: int


class UserPostwithComments(BaseModel):
    post: UserPost
    comments: list[Comment]
