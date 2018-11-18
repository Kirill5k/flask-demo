from flask import request, Blueprint
from auth.services import AuthService
from utils.http import res_error, res_success

auth = Blueprint('auth', __name__, url_prefix='/auth')

auth_service = AuthService()


@auth.route('/login', methods=['POST'])
def login():
    try:
        request_data = request.get_json()
        token = auth_service.login(request_data['username'], request_data['password'])
        message = {'token': f'Bearer {token}'}
        return res_success(message)
    except ValueError:
        return res_error('username or password is incorrect', status=400)


@auth.route('/register', methods=['POST'])
def register():
    try:
        new_user = request.get_json()
        auth_service.register(new_user)
        return res_success(status=201)
    except ValueError as error:
        return res_error(error, status=409)
