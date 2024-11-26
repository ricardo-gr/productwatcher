from flask import Blueprint, render_template, send_file
from .models import load_product_listing
from config import Config

# Create a blueprint for routes
main = Blueprint('main', __name__)

@main.route('/')
def index():
    products = load_product_listing()
    return render_template('index.html', products=products, title=Config.WEBPAGE_TITLE)
