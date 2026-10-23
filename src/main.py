import my_test

try:
    from PIL import ImageGrab
    import screeninfo
    import pytesseract

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")


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
        test_main()        
        

main()
