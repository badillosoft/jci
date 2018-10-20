from flask import Flask
from flask import request
from flask import render_template
import json
import os
# sudo python -m pip install flask-cors
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/")
def home():
    	return render_template("index.html")

@app.route("/<name>")
def job(name):
	data = ""
	try:
		data = request.args.to_dict()
	except:
		pass
	cmd = "python jobs/{}.py '{}'".format(name, json.dumps(data))
	stream = os.popen(cmd)
	return stream.read()


app.run(port=80)
