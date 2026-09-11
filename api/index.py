import os
import sys

# Ensure the project root is in sys.path so modules like app.py can be imported
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# Import the Flask WSGI instance
from app import app

# Vercel's Python runtime inspects and invokes `app`
if __name__ == "__main__":
    app.run(debug=True)
