import flask
import flask_restful
import os
from http import HTTPStatus
from . import models, session
from . import helpers
from .constants import CONSTANTS


class SignUp(flask_restful.Resource):  # create user
    def post(self):
        json = flask.request.json
        fields = ['user', 'password']
        helpers.check_for_missing_fields_or_404(json, fields)
        user, password = map(lambda x: json[x], fields)
        users_with_same_name = models.User.query.filter(models.User.name == user).all()

        if len(users_with_same_name) > 0:
            return 'name already in use', HTTPStatus.CONFLICT

        else:
            salt = helpers.generate_cryptographically_random_string(8)
            hashed_password = helpers.hash_with_salt(password, salt)
            new_user = models.User(name=user, password=hashed_password, salt=salt)
            session.add(new_user)
            token = helpers.generate_jwt(new_user)
            session.commit()
            return {'token': token}, HTTPStatus.CREATED


class SignIn(flask_restful.Resource):  # login
    def post(self):
        json = flask.request.json
        fields = ['user', 'password']
        helpers.check_for_missing_fields_or_404(json, fields)
        username, password = map(lambda x: json[x], fields)
        users_with_same_name = models.User.query.filter(models.User.name == username).all()

        print(users_with_same_name)

        if len(users_with_same_name) == 0:
            return self.error()

        else:
            user = users_with_same_name[0]
            salt = user.salt
            hashed_password = helpers.hash_with_salt(password, salt)

            print('  stored:', user.password, user.salt)
            print('computed:', hashed_password)

            if hashed_password == user.password:
                token = helpers.generate_jwt(user)
                return {'token': token}, HTTPStatus.ACCEPTED
            else:
                return self.error()

    def error(self):
        return 'Invalid username or password', HTTPStatus.UNAUTHORIZED


class Items(flask_restful.Resource):
    def get(self):  # get catalog
        catalogs = models.Catalog.query.all()
        cat_info = {}
        for catalog in catalogs:
            items = []
            for item in catalog.items:
                item_info = {
                    'name': item.name,
                    'description': item.description,
                    'value': item.value,
                    'image': item.image,
                    'id': item.id
                }
                items.append(item_info)
            cat_info[catalog.name] = items

        return cat_info, HTTPStatus.OK

    def post(self):  # add or edit item
        json = flask.request.json
        fields = ['token', 'name', 'description', 'value', 'catalog']
        helpers.check_for_missing_fields_or_404(json, fields)
        token, name, description, value, catalog_name = map(lambda x: json[x], fields)

        try:
            user_id, _ = helpers.decode_jwt(token)
            user_db = models.User.query.filter(models.User.id == user_id).first()
        except:
            return 'Invalid token', HTTPStatus.UNAUTHORIZED

        try:
            value = float(value)
        except ValueError:
            return 'Value field is invalid', HTTPStatus.NOT_ACCEPTABLE

        catalogs_db = models.Catalog.query.filter(models.Catalog.name == catalog_name).all()
        if len(catalogs_db) == 0:
            # create catalog
            catalog_db = models.Catalog(name=catalog_name, owner=user_db)
            session.add(catalog_db)
        else:
            catalog_db = catalogs_db[0]
            if catalog_db.owner != user_db:
                return 'You do not own this catalog', HTTPStatus.FORBIDDEN

        items_with_name = models.Item.query.filter(models.Item.name == name).filter(models.Item.catalog.owner == user_db).all()
        
        if len(items_with_name) > 0:
            created = False
            item = items_with_name[0]

            item.description = description
            item.value = value
            item.catalog = catalog_db

        else:
            created = True
            item = models.Item(name=name, description=description, value=value, catalog=catalog_db)

        session.add(item)
        session.commit()
        return 'Item added' if created else 'Item updated', HTTPStatus.OK

    def put(self):  # buy
        json = flask.request.json
        fields = ['token', 'item_id']
        helpers.check_for_missing_fields_or_404(json, fields)
        token, item_id = map(lambda x: json[x], fields)

        try:
            user_id, _ = helpers.decode_jwt(token)
            user_db = models.User.query.filter(models.User.id == user_id).first()
        except:
            return 'Invalid token', HTTPStatus.UNAUTHORIZED

        item_db = models.Item.query.filter(models.Item.id == item_id).first_or_404()

        transaction = models.Transaction(item=item_db, user=user_db)
        session.add(transaction)
        session.commit()

        return f'item {item_db.name} bought', HTTPStatus.OK


class Files(flask_restful.Resource):
    def post(self, filename):
        """Upload a file."""

        if "/" in filename:
            # Return 400 BAD REQUEST
            return "no subdirectories directories allowed", HTTPStatus.BAD_REQUEST

        with open(os.path.join('.', CONSTANTS.upload_dir, filename), "wb") as fp:
            fp.write(flask.request.data)

        # Return 201 CREATED
        return "ok", HTTPStatus.CREATED
