from ultim8x8 import ULTiM8x8, ULTiM8x24, ULTiM8x72, ULTiM24x24, ULTiM16x56 
from bibliopixel import log
from BiblioPixelAnimations.matrix.ScreenGrab import ScreenGrab
log.setLogLevel(log.DEBUG)


## change this line to indentify your serial USB port
dev = '/dev/ttyACM0'

## change this line as appropropriate for your array
led = ULTiM16x56(dev)
led.setMasterBrightness(16) ## use low brightness (<5) for running off of USB

try:
    ## define screen grab region
    scale = 8  ## screen pixels per array pixel
    xoff = 200 ## left
    yoff = 300 ## top
    
    anim = ScreenGrab(led, bbox=(xoff, xoff,
                                 xoff + led.width * scale,
                                 yoff + led.height * scale), mirror=False)
    anim.run(fps=10)
except KeyboardInterrupt:
    ## Quietly exit with keyboard interrupt (CTRL-C)
    pass
finally:
    led.all_off()
    led.update()
