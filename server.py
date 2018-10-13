from flask import Flask
from flask import request
import json
import os
# python -m pip install flask-cors
from flask_cors import CORS

app = Flask(__name__)

CORS(app)

@app.route("/<name>")
def job(name):
	data = ""
	try:
		data = json.dumps(request.form)
	except:
		pass
	cmd = "python jobs/{}.py {}".format(name, data)
	stream = os.popen(cmd)
	return stream.read()


app.run(port=80)
