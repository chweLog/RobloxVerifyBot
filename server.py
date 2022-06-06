from flask import Flask,request
from threading import Thread
import os

app = Flask('')

@app.route('/api', methods=['POST'])
def api():
  params = request.get_json()
  try:
    data = f"./{params['name'].lower()}.txt"
    os.remove(f"./{params['name'].lower()}.txt")
    return 'success'
  except:
    return 'fail'

def run():
  app.run(host='0.0.0.0',port=8080)

def run_server():
    t = Thread(target=run)
    t.start()

