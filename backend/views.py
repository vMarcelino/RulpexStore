import flask
import flask_restful
from http import HTTPStatus
from backend import models, session

def check_for_missing_fields_or_404(json, fields):
    for field in fields:
        if field not in json:
            flask.abort(404)


class SingUp(flask_restful.Resource):
    def put(self):
        json = flask.request.json
        fields = ['user', 'password']
        check_for_missing_fields_or_404(json, fields)
        user, password = map(lambda x: json[x], fields)
        users_with_same_name = models.User.query.filer(models.User.name == user).all()

        if len(users_with_same_name) > 0:
            return 'name already in use', HTTPStatus.CONFLICT

        else:
            new_user = models.User(name=user, password=password)
            session.add(new_user)
            id = new_user.id

