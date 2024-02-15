from flask import Flask, request, jsonify
import csv
from datetime import datetime, timedelta
import redis
import json


r = redis.Redis(host='localhost', port=6379, db=0)

app = Flask(__name__)

events_db = []

if __name__ == '__main__':
    app.run(debug=True, port=5000)

@app.route('/operation', methods=['GET'])
def get_result_from_id():
    id = request.args.get('id')
    operation_result = r.get(id)
    if operation_result:
        return operation_result
    else:
        return "Event not found", 404
    
