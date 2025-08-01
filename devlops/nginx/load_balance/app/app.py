# app/app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
  return f"Hello from instance: {os.environ.get('HOSTNAME', 'Unknown')}"

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)