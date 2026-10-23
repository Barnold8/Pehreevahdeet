from PIL import ImageGrab
import screeninfo

#TODO: get screen information and make it cross platform


def getScreen(monitor:Monitor):

    screen = ImageGrab.grab(all_screens=True,bbox=(
    
                monitor.x,
                monitor.y,
                monitor.x + monitor.width,
                monitor.y + monitor.height
        
            )
    )
    screen.show()

monitors = screeninfo.get_monitors()

for screen in monitors:

    print(f"(x,y) = {screen.x},{screen.y} | (w,h) = {screen.width},{screen.height}")


getScreen(monitors[1])

