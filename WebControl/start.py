from flask import Flask, render_template, jsonify
from tmpg import get_temp
import RPi.GPIO as GPIO
import time

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("TEST.html")

@app.route("/on")
def on():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.HIGH)
    return render_template("TEST.html")

@app.route("/off")
def off():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(4,GPIO.OUT)
    GPIO.output(4,GPIO.LOW)
    return render_template("TEST.html")

@app.route("/tmp_info", methods=['GET', 'POST'])
def tmp_info():
    tmp, hum = get_temp()
    tmp_info = {'tmp': tmp, 'hum': hum}
    return jsonify(tmp_info)


if __name__=="__main__":
    app.run(host='0.0.0.0', port=8888, debug=True)
