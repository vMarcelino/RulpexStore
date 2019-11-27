import datetime
import jwt
import string
import secrets
import hashlib
import flask
from .constants import CONSTANTS


def check_for_missing_fields_or_404(json, fields):
    for field in fields:
        if field not in json:
            flask.abort(404)


def generate_jwt(user):
    payload = {'sub': user.id, 'name': user.name, 'iat': datetime.datetime.utcnow()}
    return jwt.encode(payload=payload, key=CONSTANTS.key, algorithm='HS256').decode()


def decode_jwt(jwt_token):
    payload = jwt.decode(jwt=jwt_token, key=CONSTANTS.key, algorithms='HS256')
    return payload['sub'], payload['name']


def hash_with_salt(payload, salt):
    return hashlib.sha512((payload + salt).encode()).hexdigest()


def generate_cryptographically_random_string(len: int = 8) -> str:
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for i in range(len))