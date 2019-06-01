#
#   My Python program to act as a set of trafficlights.
#   Could use actual light timings, but it is new. :)
#

import RPi.GPIO as GPIO
import time
import sys
from colorama import Fore, Back, Style

# Initializing the pins
red = 7
yellow = 11
green = 12
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(12, GPIO.OUT)


# Green light duration
def green_led(g):
    print(Fore.GREEN + '\n[*] Green pin is lit fam\n')
    GPIO.output(green, GPIO.HIGH)
    time.sleep(120)
    GPIO.output(green, GPIO.LOW)
    print '\n[*] Green pin is dead yo\n'
    print(Style.RESET_ALL)
    return

# Yellow light duration
def yellow_led(y):
    print '\n[*] Yellow pin is lit fam\n'
    GPIO.output(yellow, GPIO.HIGH)
    time.sleep(8)
    GPIO.output(yellow, GPIO.LOW)
    print '\n[*] Yellow pin is dead yo\n' 
    print(Style.RESET_ALL)
    return

# Red light duration
def red_led(r):
    print '\n[*] Red pin is lit fam\n'
    GPIO.output(red, GPIO.HIGH)
    time.sleep(120)
    GPIO.output(red, GPIO.LOW)
    print '\n[*] Red pin is dead yo\n'
    print(Style.RESET_ALL)
    return

# Main Logic
def main():
    mode = GPIO.getmode()
    print '[', mode, '] is the Board mode\n'
    time.sleep(2)
    print '\n#######################'
    print '# Traffic has started #'
    print '#######################\n'

    # Loop for a really long time.
    for i in range(0, 999999):
        green_led(red)
        yellow_led(yellow)
        red_led(green)
    GPIO.cleanup(red)
    GPIO.cleanup(yellow)
    GPIO.cleanup(green)


if __name__ == "__main__":
    # A fun keyboard interrupt complete
    # with a nice message
    try:
        main()
    except KeyboardInterrupt:
        print '\n######################'
        print '# Killed by keyboard #'
        print '######################\n'
        GPIO.cleanup(red)
        GPIO.cleanup(yellow)
        GPIO.cleanup(green)
        sys.exit(1)
