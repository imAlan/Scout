from flask import Flask
from flask_foundation import Foundation

app = Flask(__name__)
foundation = Foundation(app)

from config import *

app.config.from_object('config')

from app.models import db
db.init_app(app)

from app import views