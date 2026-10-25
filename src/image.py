
import os
import io
import base64
import requests
from PIL import Image

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


def getScreen(monitor:Monitor)-> PIL.Image.Image: # what in the world is that type? Image file with an Image class?

    screen = ImageGrab.grab(all_screens=True,bbox=(
    
                monitor.x,
                monitor.y,
                monitor.x + monitor.width,
                monitor.y + monitor.height
        
            )
    )
    return screen 

