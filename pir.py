import datetime
from gpiozero import MotionSensor
import subprocess

def takePhoto():
	print("Take photo...")
	# cmd = ['ls', '-l']
	# cmd = ['raspistill', '-o', out_file, '-w', '720', '-h', '720', '-hf', '-vf']
	cmd = ['/bin/bash', '/home/pi/scripts/photo.sh', 'pir']
	runProcessNoWait(cmd)

def runProcessNoWait(cmd):
	process = subprocess.Popen(cmd)


GPIO_PIN = 4
pir = MotionSensor(GPIO_PIN)

while True:
    print("Wait for motion...")
    pir.wait_for_motion()
    print("You moved")
    takePhoto()
    print(datetime.datetime.utcnow())
    print("Wait for no motion")
    pir.wait_for_no_motion()
