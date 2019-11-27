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
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_ECHO'] = True
api = flask_restful.Api(app)
dbapp = flask_sqlalchemy.SQLAlchemy(app)

session = dbapp.session

from . import models as models
from . import views
from .constants import CONSTANTS

api.add_resource(views.SignIn, '/signin')
api.add_resource(views.SignUp, '/signup')
api.add_resource(views.Items, '/item')
api.add_resource(views.Files, '/upload_file/<filename>')


@app.route("/download_file/<path:path>")
def get_file(path):
    """Download a file."""
    return flask.send_from_directory(CONSTANTS.upload_dir, path, as_attachment=True)


def main(host, port):
    app.run(host=host, port=port, debug=False)


if __name__ == '__main__':
    main(host='0.0.0.0', port=2281)
