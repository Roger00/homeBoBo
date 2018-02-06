import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
from sys import argv

OUTPUT_PIN_PWM = 18
OUTPUT_PIN_2 = 14
OUTPUT_PIN_3 = 15

def startWheels():
    print 'Run the wheels'

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(OUTPUT_PIN_PWM, GPIO.OUT)
    GPIO.setup(OUTPUT_PIN_2, GPIO.OUT)
    GPIO.setup(OUTPUT_PIN_3, GPIO.OUT)

    p = GPIO.PWM(OUTPUT_PIN_PWM, 50)
    p.start(50)

    # GPIO.output(OUTPUT_PIN_PWM, GPIO.HIGH)
    GPIO.output(OUTPUT_PIN_2, GPIO.HIGH)
    GPIO.output(OUTPUT_PIN_3, GPIO.HIGH)

def main():
    try:
        startWheels()
        sleep(20)

    except KeyboardInterrupt:
        print 'interrupt'

    GPIO.cleanup()

    print 'End script'

if __name__ == '__main__':
    main()

