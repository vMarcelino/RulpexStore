import flask
import flask_sqlalchemy
import flask_restful
# import flask_httpauth

import travel_backpack
import os
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'store.db')

app = flask.Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
#app.config['SQLALCHEMY_ECHO'] = True
api = flask_restful.Api(app)
dbapp = flask_sqlalchemy.SQLAlchemy(app)

session = dbapp.session

from financesSQL import models as models
from financesSQL import views



api.add_resource(views.Notificacao, '/notificacao')


def main():
    app.run(host='0.0.0.0', port=2281, debug=False, extra_files=ef)


if __name__ == '__main__':
    main()
