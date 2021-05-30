from pymata4 import pymata4
import time

carte = pymata4.Pymata4()


DELAY = 0.5 
PIN = 13

carte.set_pin_mode_digital_output(PIN)

def blink():
    print('ON')
    carte.digital_write(PIN, 1)
    time.sleep(DELAY)
    print('OFF')
    carte.digital_write(PIN, 0)
    time.sleep(DELAY)

try:
    while True:
        blink()
except KeyboardInterrupt: # Ctrl+C
    carte.shutdown()
    sys.exit(0)
finally:
    carte.shutdown()  
