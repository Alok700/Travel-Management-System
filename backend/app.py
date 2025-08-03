# from flask import Flask, jsonify
# from flask_cors import CORS
# from sqlalchemy import create_engine, text
# from dotenv import load_dotenv
# import os

# # ✅ Load environment variables
# load_dotenv()

# app = Flask(__name__)
# CORS(app)

# # ✅ Database URL from .env
# DATABASE_URL = os.getenv("DATABASE_URL")

# # ✅ SQLAlchemy engine
# engine = create_engine(DATABASE_URL)

# # ✅ Route: Home
# @app.route('/')
# def home():
#     return jsonify({"message": "Backend running!"})

# # ✅ Route: Get all locations
# @app.route('/locations')
# def get_locations():
#     try:
#         with engine.connect() as conn:
#             result = conn.execute(text("SELECT * FROM locations")).mappings()
#             data = [dict(row) for row in result]
#         return jsonify(data)
#     except Exception as e:
#         return jsonify({"error": str(e)})

# # ✅ Run the server
# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, jsonify, request
from flask_cors import CORS
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
CORS(app)

DATABASE_URL = os.getenv("DATABASE_URL")
engine = create_engine(DATABASE_URL)

@app.route('/')
def home():
    return jsonify({"message": "Backend running!"})

@app.route('/locations')
def get_locations():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM locations")).mappings()
            data = [dict(row) for row in result]
        return jsonify(data)
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/add-location', methods=['POST'])
def add_location():
    try:
        data = request.json
        query = text("""
            INSERT INTO locations (name, latitude, longitude, description)
            VALUES (:name, :lat, :lon, :desc)
        """)
        with engine.connect() as conn:
            conn.execute(query, {
                "name": data["name"],
                "lat": data["latitude"],
                "lon": data["longitude"],
                "desc": data["description"]
            })
            conn.commit()
        return jsonify({"message": "Location added!"})
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == '__main__':
    app.run(debug=True)
