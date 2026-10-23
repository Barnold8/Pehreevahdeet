from PIL import ImageGrab


def getScreen(resX:int,resY:int,monitor:int):

    monitor = monitor+1
    #screen =  ImageGrab.grab(bbox=(resX,0,resX*monitor+resX,resY),all_screens=True)
    screen = ImageGrab.grab(all_screens=True)
    screen.show()


getScreen(1920,1080,1)

