from PIL import ImageGrab
import screeninfo

#TODO: get screen information and make it cross platform
 
def getScreen(resX:int = 1920,resY:int = 1080,monitor:int = 0):

    monitorStartX = resX * monitor
    monitorStartY = 0 # because assuming monitors are all on the same Y axis (not the case for monitor set ups where one is higher than others)
    monitorEndX = resX
    monitorEndY = resY

    print(f"({monitorStartX},{monitorStartY})|({monitorEndX},{monitorEndY})")

    #screen = ImageGrab.grab(all_screens=True,bbox=(1920,0,1920*2,1080))

    screen = ImageGrab.grab(all_screens=True,bbox=(monitorStartX,0,monitorEndX+(monitor*monitorEndX),monitorEndY))
    screen.show()

getScreen(1920,1080,1)


