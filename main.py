import math
import time
import config
import RPi.GPIO as GPIO
from flask import Flask
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
global curentStep
curentStep = 0
#distance in mm
def move(dis, timeToNextImg = 2):
	#0,07568359375 mm /step
	steps = math.floor(dis / 0.07568359375)
	sleepTime = timeToNextImg/steps
	print (steps)
	if sleepTime < 0.002:
		sleepTime = 0.002


	seq=[[1,1,0,0],[0,1,1,0],[0,0,1,1],[1,0,0,1]]
	while (steps > 0):
		global curentStep
		print (seq[curentStep])
		#match seq to pins to move
		for pig in range(4):
                	GPIO.output(config.controlPin[pig], seq[curentStep][pig])
		if curentStep == 3:
			curentStep = 0
		else:
			curentStep += 1
		steps -=1
		#print(sleepTime)
		time.sleep(sleepTime)
	return True


def movePic():
	totalDis = 100
	pictures = 10
	interval = 2
	distansmoved = 0

	while (distansmoved < totalDis):
		#ta bild
		
		print (distansmoved)
		time.sleep(2)
		distansToMove = totalDis/pictures
		if (totalDis-distansmoved > distansToMove):
			move(distansToMove, interval)
			distansmoved += distansToMove
		elif (distansmoved < totalDis):
			move(totalDis-distansmoved, interval)
			distansmoved += totalDis-distansmoved
		else:
			return True
	GPIO.cleanup()
def init():
	for pin in config.controlPin:
		GPIO.setup(pin,GPIO.OUT)
		GPIO.output(pin,0)

	global app
	@app.route("/")
	def index():
		return "working"
	app.run(host= '0.0.0.0', debug=True)
	movePic()
init()

