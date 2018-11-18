import jwt
import datetime as dt
from auth.repositories import UserRepository
from auth.domain import User
from config import SECRET_KEY


class UserService:
    __user_repo = UserRepository()

    def get_by_name(self, name):
        return self.__user_repo.get_by_name(name)

    def create(self, new_user_payload):
        new_user = User(None, new_user_payload['username'], new_user_payload['password'])
        self.__user_repo.create(new_user)


class AuthService:
    __user_service = UserService()

    @staticmethod
    def __generate_token():
        expiration_date = dt.datetime.utcnow() + dt.timedelta(seconds=3600)
        token_bytes = jwt.encode({'exp': expiration_date}, SECRET_KEY, algorithm='HS256')
        return token_bytes.decode()

    def login(self, username, password):
        user = self.__user_service.get_by_name(username)
        if user.password == password:
            return self.__generate_token()
        else:
            raise ValueError('incorrect password')

    def register(self, new_user):
        self.__user_service.create(new_user)

    @staticmethod
    def is_authorized(token):
        try:
            jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            return True
        except (jwt.ExpiredSignatureError, jwt.DecodeError):
            return False
