from flask_frozen import Freezer
from app import app  # Import your Flask app

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.register_generator('/')
    freezer.register_generator('/quiz')
    freezer.register_generator('/about')
    freezer.register_generator('/contact')
    freezer.add_static_rule('/styles', 'styles')
    freezer.add_static_rule('/images', 'images')
    freezer.freeze()