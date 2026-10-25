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

def errPrint(*args:str, **kwargs:str)->None:
    print(*args, file=sys.stderr, **kwargs)

def imageToBase64(image: PIL.Image.Image) -> str:
    
    buffer = io.BytesIO()
    image.save(buffer, format="PNG")
    img_bytes = buffer.getvalue()
    base64_str = base64.b64encode(img_bytes).decode('utf-8')
    return f"data:image/png;base64,{base64_str}"

def OCR(image: PIL.Image.Image, api_key: str, isOverlay: bool = False, lang: str = 'eng'):
    API_URL = 'https://api.ocr.space/parse/image'
        

    payload = {
         'apikey': api_key,
         'base64Image': imageToBase64(image),
         'isOverlayRequired': str(isOverlay).lower(), 
         'language': lang 
    }
    r = requests.post(
        API_URL,
        data=payload
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
                key =  file.readlines()[0]
                return  ''.join(key.split())
            except IndexError:
                errPrint(f"Error: {path} is either empty or corrupt")
    except FileNotFoundError as FNFE:
        errPrint(f"Error: {path} does not exist")


def main():
    
    if __name__ == "__main__":

        #monitors = screeninfo.get_monitors()
        #img = getScreen()
        #x.show()
        #print("Grabbing images")
        
        images = loadImages("samples")
        KEY = getAPIKey('API_KEY')
        for img in images:
            print(OCR(img,KEY))

main()
