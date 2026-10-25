try:
    # Needed lib code
    import time
    # My own code
    import utils
    import image

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")

def sleepInNano(nano_seconds: int)-> None:
    time.sleep(nano_seconds/1000000.0)
  
def main():
   
    POLL_RATE = 50

    if __name__ == "__main__":

                images = image.loadImages("samples")
        KEY = utils.getAPIKey('API_KEY')
        for img in images:
            print(image.OCR(img,KEY))

main()
