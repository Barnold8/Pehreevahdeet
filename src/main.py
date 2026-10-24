try:

    from PIL import ImageGrab
    from PIL import Image
    import screeninfo

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")


#TODO: find some easy way of setting up OCR on a system that isnt a headache

def getScreen(monitor:Monitor)-> PIL.Image.Image: # what in the world is that type? Image file with an Image class?

    screen = ImageGrab.grab(all_screens=True,bbox=(
    
                monitor.x,
                monitor.y,
                monitor.x + monitor.width,
                monitor.y + monitor.height
        
            )
    )
    return screen 

def loadImages(path:str):

    PATH   = path
    files  = []
    images = []

    
    for (dirpath, dirnames, filenames) in walk(path):
        files.extend(filenames)

    if len(files) <= 0:
        print(f"Warning: no files found in {path}")
        return files

    for img in files:
        fPath = f"{path}/{img}"
        images.append(Image.open(fPath))

    return images

def main():
    
    if __name__ == "__main__":

        if not isTesseract():
            return -1
        
        #monitors = screeninfo.get_monitors()
        #img = getScreen()
        #x.show()
        print("Grabbing images")

        images = loadImages("samples")

main()
