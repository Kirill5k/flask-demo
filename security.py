from flask import request
from auth.services import AuthService
from utils.http import res_error
from functools import wraps

AUTH_TYPE = 'Bearer '

auth_service = AuthService()


def authorized(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        token_header = request.headers.get('Authorization', None)
        if not token_header:
            return res_error('Authroization header is required', status=403)
        if not token_header.startswith(AUTH_TYPE):
            return res_error('unsupported authorisation type', status=400)
        token  = token_header.split(AUTH_TYPE)[1]
        if not auth_service.is_authorized(token):
            return res_error('not authorised', status=403)
        return f(*args, **kwargs)
    return wrapper
