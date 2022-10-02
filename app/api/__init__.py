from flask import Blueprint

bp = Blueprint('api', __name__)

from app.api.telegram.bots import moderator
from app.api.orders.transactions.hotmart import purchase_approved