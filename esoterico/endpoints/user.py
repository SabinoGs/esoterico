from fastapi import APIRouter
from esoterico.models.user import UserInModel
from esoterico.services.user import UserService

user_app = APIRouter()



@user_app.post('/user', response_model=UserInModel)
def register_user(response: UserInModel):
    user_client = UserService(response)
    user = user_client.register_user()

    return user

