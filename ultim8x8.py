from pixel_maps import  ultim8x8, ultim8x24, ultim8x72, ultim24x24, ultim16x56
from bibliopixel.drivers.serial_driver import DriverSerial, LEDTYPE
from bibliopixel import LEDMatrix, log
from BiblioPixelAnimations.matrix.ScreenGrab import ScreenGrab

def getPixelArray(pixel_map, dev):
        '''
        pixel_map -- MultiMap Builder
        dev -- com port ident string
        '''
        width = len(pixel_map.map[0])
        height = len(pixel_map.map)
        n_pixel = width * height
        driver = DriverSerial(LEDTYPE.GENERIC,
                              n_pixel,
                              hardwareID="16C0:0483",
                              dev=dev)
        led = LEDMatrix(driver,
                        width=width,
                        height=height,
                        coordMap=pixel_map.map)
        return led

def ULTiM8x8(dev):
    pixel_map = ultim8x8         
    return getPixelArray(pixel_map, dev)

def ULTiM8x24(dev):
    pixel_map = ultim8x24         
    return getPixelArray(pixel_map, dev)

def ULTiM8x72(dev):
    pixel_map = ultim8x72        
    return getPixelArray(pixel_map, dev)

def ULTiM24x24(dev):
    pixel_map = ultim24x24        
    return getPixelArray(pixel_map, dev)

def ULTiM16x56(dev):
    pixel_map = ultim16x56
    return getPixelArray(pixel_map, dev)

        
