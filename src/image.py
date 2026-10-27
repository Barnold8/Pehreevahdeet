import io
import base64
import requests
import json
import numpy as np
import settings
from PIL import Image, ImageGrab,ImageChops

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

    width  = settings.Image.SCREENSHOT_AREA[0]
    height = settings.Image.SCREENSHOT_AREA[1]

    screen = ImageGrab.grab(all_screens=True,bbox=(
    
                monitor.x,
                monitor.y,
                monitor.x + width,
                monitor.y + height
        
            )
    )
    return screen 

def getMessage(unserialised:str) -> List[str]:
    try:
        payload = json.loads(unserialised)["ParsedResults"]
        payload = payload[0]
        payload = payload["ParsedText"]
        return payload.split("\n")
        
    except KeyError as KE:
        errPrint(f"getMessage | Error: could not read from the OCR API output.\n\nFULL ERROR: {KE}")

def getImageDiff(img1:PIL.Image.Image,img2:PIL.Image.Image)->float:

    if img1.size != img2.size or img1.mode != img2.mode:
        raise ValueError("getImageDiff | Error: Images must have the same dimensions and color mode.")

    diff = ImageChops.difference(img1, img2)
    if diff.getbbox() is None:
        return 0.0
    else:
        diff_array = np.array(diff)
        total_actual_diff = np.sum(diff_array)
        max_possible_diff = diff_array.size * 255
        percentage_diff = (total_actual_diff / max_possible_diff) * 100    
        similarity_percentage = 100.0 - percentage_diff
        return float(similarity_percentage) 

def safeGuardMonitorIndex(monitors,index:int) -> int:

    if index > len(monitors):
        if settings.Screen.PREFER_FIRST_MONITOR:
            return 0
        else:
            return len(monitors) - 1
    return index

