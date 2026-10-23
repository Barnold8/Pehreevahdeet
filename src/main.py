import venvpro as vp

try:
    from PIL import ImageGrab
    import screeninfo

except ModuleNotFoundError as MNFE:
    print("ERROR")

#TODO force venvpro in a main function to make user process easier

def getScreen(monitor:Monitor)-> PIL.Image.Image: # what in the world is that type? Image file with an Image class?

    screen = ImageGrab.grab(all_screens=True,bbox=(
    
                monitor.x,
                monitor.y,
                monitor.x + monitor.width,
                monitor.y + monitor.height
        
            )
    )
    return screen 

def main():
    
    if __name__ == "__main__":
        
        vp.venv("venv",[],"requirements.txt")

        
        pass
        #monitors = screeninfo.get_monitors()

        #x = getScreen(monitors[1])
        #x.show()



main()
