import RPi.GPIO as GPIO            # import RPi.GPIO module  
from time import sleep             # lets us have a delay  
from sys import argv
from readchar import readkey
import cPickle as pickle
import datetime

OUTPUT_PIN = 18
COUNTER_FILE = "counter.pickle"

UP = '\x1b[A'
DOWN = '\x1b[B'
RIGHT = '\x1b[C'
LEFT = '\x1b[D'

DIRECT_KEYS = [UP, DOWN, LEFT, RIGHT]

INCREMENT = .01
STEP = 10

MIN_CYCLE = 3.3
MAX_CYCLE = 12.5

def getCycle(angle):
    return max(MIN_CYCLE, min(MIN_CYCLE + angle, MAX_CYCLE))

def doKey(last_angle, key, p):
    angle = last_angle

    if key == UP:
        print('UP')
    elif key == DOWN:
        print('DOWN')
    elif key == LEFT:
        print('LEFT')
        angle += INCREMENT * STEP
    elif key == RIGHT:
        print('RIGHT')
        angle -= INCREMENT * STEP

    lastCycle = getCycle(last_angle)
    cycle = getCycle(angle)

    # persist last angle if out of range
    if abs(lastCycle - cycle) < 0.01:
        angle = last_angle
    
    p.ChangeDutyCycle(cycle)
    print 'Change duty cycle: ', cycle

    return angle

def key_adjust(last_angle, p):
    print('Start reading keys...')

    while 1:
        key = readkey()
        print key
        if key not in DIRECT_KEYS:
            print('This must be return signal' + key)
            break
        else:
            last_angle = doKey(last_angle, key, p)

    return last_angle

def saveObj2Pickle(dumpFilePath, obj):
    ''' Save a single object to pickle file '''
    try:
        print '[saveObj2Pickle] pickle path: %s' % (dumpFilePath,)
        pickle.dump(obj, open(dumpFilePath, 'wb'), pickle.HIGHEST_PROTOCOL)
    except IOError:
        print '[saveObj2Pickle] Error: fail to open or save to setting file'
    except pickle.PicklingError:
        print '[saveObj2Pickle] Error: passed unpicklable object'

def readObjFromPickle(dumpFilePath, default=None):
    ''' Read a single object from pickle file '''
    obj = default
    try:
        print '[readObjFromPickle] read from: %s' % (dumpFilePath,)
        obj = pickle.load(open(dumpFilePath, 'rb'))
    except IOError:
        print '[readObjFromPickle] Error: fail to load settings from file'
    except pickle.UnpicklingError:
        print '[readObjFromPickle] Error: there is a problem unpickling the setting file'

    return obj

def lightOn():
    print 'Feed the fish, run the wheels'

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(OUTPUT_PIN, GPIO.OUT)

    last_angle = readObjFromPickle(COUNTER_FILE, 0)
    print 'Last cycle is: ', last_angle
    
    p = GPIO.PWM(OUTPUT_PIN, 50)
    p.start(getCycle(last_angle))

    try:
        last_angle = doKey(last_angle, RIGHT, p)
        last_angle = doKey(last_angle, RIGHT, p)

    except KeyboardInterrupt:
        p.stop()
        GPIO.cleanup()

    saveObj2Pickle(COUNTER_FILE, last_angle)

    print 'End script'

class EST(datetime.tzinfo):
    def utcoffset(self, dt):
        return datetime.timedelta(hours=+8)

    def dst(self, dt):
        return datetime.timedelta(0)

if __name__ == '__main__':
    lightOn()
