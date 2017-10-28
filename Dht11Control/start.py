from flask import Flask, render_template, jsonify
from tmpg import get_temp
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setwarnings(False)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/tmp_info", methods=['GET', 'POST'])
def tmp_info():

	tmp, hum = get_temp()
	tmp_info = {'tmp': tmp, 'hum': hum}
	return jsonify(tmp_info)


@app.route("/on")
def on():
	GPIO.output(7,GPIO.HIGH)
	return render_template("main.html")

@app.route("/off")
def off():
    GPIO.output(7,GPIO.LOW)
    return render_template("main.html")

if __name__=="__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
