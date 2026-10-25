try:
    import requests
    from PIL import ImageGrab
    from PIL import Image
    import screeninfo
    import os
    import base64
    import io
except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")


#TODO: find some easy way of setting up OCR on a system that isnt a headache

def imageToBase64(image: PIL.Image.Image):

    buffer = io.BytesIO()
    image.save(buffer,format="JPEG")
    buffer.seek(0)
    image_in_bytes = buffer.read()

    return base64.b64encode(image_in_bytes)

def OCR(image: PIL.Image.Image,api_key:str, isOverlay:bool = False,lang: str ='auto'):

    # taken from https://github.com/Zaargh/ocr.space_code_example/blob/master/ocrspace_example.py

    API_URL = 'https://api.ocr.space/parse/image'

    payload = {
            'isOverlayRequired': isOverlay,
            'apikey': api_key,
            'language': lang,
            'base64Image': {"data" : imageToBase64(image)}
    }

    r = requests.post(
            API_URL,
          
            data=payload,              
    )
    return r.content.decode()


def processImage(image: PIL.Image.Image)-> str:

    contents = ""

    return contents

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

    
    for (dirpath, dirnames, filenames) in os.walk(path):
        files.extend(filenames)

    if len(files) <= 0:
        print(f"Warning: no files found in {path}")
        return files

    for img in files:
        fPath = f"{path}/{img}"
        images.append(Image.open(fPath))

    return images

def getAPIKey(path:str)->str:

    try:
        with open(path,'r') as file:
            try:
                return file.readlines()[0]
            except IndexError:
                print(f"Error: {path} is either empty or corrupt")
    except FileNotFoundError as FNFE:
        print(f"Error: {path} does not exist")


def main():
    
    if __name__ == "__main__":

        #monitors = screeninfo.get_monitors()
        #img = getScreen()
        #x.show()
        #print("Grabbing images")

        KEY = getAPIKey('API_KEY')

        images = loadImages("samples")

        print(KEY)
        #for img in images:
            #print(OCR(img),KEY)


main()
