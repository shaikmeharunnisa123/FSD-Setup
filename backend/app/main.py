from flask import Flask, jsonify
from flask_cors import CORS
from .routes.api import api_bp
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(
    __name__,
    instance_relative_config=True
)

# Add CORS support
CORS(app)

# Register blueprints
app.register_blueprint(api_bp, url_prefix="/api")

@app.route("/")
def read_root():
    return jsonify({
        "message": "Hello World from Flask!",
        "app_name": os.getenv("APP_NAME", "Flask Backend"),
        "version": os.getenv("API_VERSION", "v1")
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000) 