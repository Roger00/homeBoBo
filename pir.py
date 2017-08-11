import datetime
from gpiozero import MotionSensor
import subprocess

def takePhoto(out_file):
	print("Take photo...save to: " + out_file)
	# cmd = ['ls', '-l']
	cmd = ['raspistill', '-o', out_file, '-w', '720', '-h', '720', '-hf', '-vf']
	runProcessNoWait(cmd)

def runProcessNoWait(cmd):
	process = subprocess.Popen(cmd)


GPIO_PIN = 4
pir = MotionSensor(GPIO_PIN)

while True:
    print("Wait for motion...")
    pir.wait_for_motion()
    print("You moved")
    takePhoto('./pir_out/what.jpg')
    print(datetime.datetime.utcnow())
    print("Wait for no motion")
    pir.wait_for_no_motion()
