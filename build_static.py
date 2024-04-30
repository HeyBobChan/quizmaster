from flask_frozen import Freezer
from app import app  # Assuming your Flask app is in a file named 'app.py'

freezer = Freezer(app)

if __name__ == '__main__':
    freezer.freeze()