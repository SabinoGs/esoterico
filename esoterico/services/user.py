from esoterico.models.user import UserInModel

class UserService():

    def __init__(self, user_model: UserInModel):
        self.user = user_model

    def register_user(self):

         return self.user
