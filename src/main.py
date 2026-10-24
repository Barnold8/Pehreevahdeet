import shutil
import os

try:
    from PIL import ImageGrab
    import screeninfo
    import pytesseract

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")


def isTesseract()-> bool:
    
    tesseract_bin = shutil.which("tesseract")
    
    if not tesseract_bin and platform.system() == "Windows":
        
        standard_windows_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        if os.path.exists(standard_windows_path):
            tesseract_bin = standard_windows_path
            pytesseract.pytesseract.tesseract_cmd = tesseract_bin
         
    if tesseract_bin:
        if "TESSDATA_PREFIX" not in os.environ:
            bin_dir = os.path.dirname(tesseract_bin)
            possible_tessdata = os.path.join(bin_dir, "tessdata")
            
            if os.path.exists(possible_tessdata):
                os.environ["TESSDATA_PREFIX"] = possible_tessdata
    else:
        print("Error: Tesseract was not found on the system. Try downloading it here: https://tesseractocr.org/install/")
        return False
    
    return True

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
        
        if not isTesseract():
            return -1
        
        #monitors = screeninfo.get_monitors()
        #img = getScreen()
        #x = getScreen(monitors[1])
        #x.show()


        pass
       

main()
