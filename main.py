from flask import Flask, request, jsonify
import csv
from datetime import datetime, timedelta
app = Flask(__name__)


events_db = []

if __name__ == '__main__':
    app.run(debug=True, port=5000)

