import time
from numpy import *
import bibliopixel.drivers.serial_driver as driver
import bibliopixel.animation as animation
import bibliopixel.led as led

raw_input('...')
s = driver.DriverSerial(driver.LEDTYPE.APA102, 64*9, dev="/dev/ttyACM0")
raw_input('0...')
led = led.LEDStrip(s)
raw_input('1...')
led.setMasterBrightness(1)
raw_input('2...')

# here

a = animation.StripChannelTest(led)
raw_input('3...')
rgb = zeros((s.numLEDs, 3), uint8)
# s.update(rgb)
led.fill((255, 0, 0))
raw_input('4...')
print dir(led)
led.update()
raw_input('5...')
for i in range(100):
    a.step()
# a.run()

