from flask import Blueprint
threat = Blueprint('threat', __name__)

from views import feed
from views import ranklist
