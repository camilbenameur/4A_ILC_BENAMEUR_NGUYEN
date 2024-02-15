from flask import Flask, request, jsonify
import csv
from datetime import datetime, timedelta
import redis


r = redis.Redis(host='localhost', port=6379, db=0)

# Ajout de variable
r.set('0', '2')                 # Retourne True si réussite

# Lecture de 
value = r.get('0')                        # Retourne la value de foo
print(value)


# app = Flask(__name__)


# events_db = []

# if __name__ == '__main__':
#     app.run(debug=True, port=5000)

