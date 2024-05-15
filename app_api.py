from flask import Flask, request, jsonify, send_file, send_from_directory
from flask_cors import CORS
from app import fetch_poster, event_filter, recommend

app = Flask(__name__)
CORS(app)

@app.route('/api/fetch/<id>', methods=['POST'])
def fetch(id):
    name, image_url, venues, startTime, info = fetch_poster(id)
    return{
        "name": name,
        "image": image_url,
        "venues": venues,
        "startTime": startTime,
        "info": info
    }

@app.route('/api/filter/<text>', methods=['POST'])
def filter(text):
    eventList = event_filter(text)
    return{
        "eventList": eventList
    }

@app.route('/api/recommend/<name>', methods=['POST'])
def get_recommend(name):
    eventList = recommend(name)
    return{
        "eventList": eventList
    }

if __name__ == '__main__':
    app.run()