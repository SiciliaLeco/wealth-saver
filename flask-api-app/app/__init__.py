from flask import Flask
from app.routes import api
from app.models import db
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

app.config.from_object('config.Config')
db.init_app(app)
app.register_blueprint(api)

with app.app_context():
    db.create_all()
