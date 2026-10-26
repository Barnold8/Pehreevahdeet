try:
    import utils
    import image as img
    import translation as tn
    from PIL import Image

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code. Have you activated the venv?\n\nHave you ran pip install -r requirements.txt while in said venv?\n\nERROR:{MNFE}")

class Settings:

    RUN_COUNT = NONE
    

def loadConfig(path:str) ->:

    pass
  
def main():
   
    POLL_RATE           = 50
    running             = True
    OCR_KEY             = utils.getAPIKey('API_KEY_OCR')
    TRANSLATION_KEY     = utils.getAPIKey('API_KEY_TRANSLATE')
    prev_img            = None
    threshold           = 50.0

    if __name__ == "__main__":

        monitors = utils.getMonitors()

        while(running):

            utils.sleepInNano(POLL_RATE) # free up cpu usage
            screen      = img.getScreen(monitors[0])
            diff        = img.getImageDiff(screen,prev_img) if prev_img != None else 0   
            if prev_img == None or diff > threshold:
                prev_img    = screen
                out         = img.OCR(screen,OCR_KEY)
                text        = img.getMessage(out)
                
                for sentence in utils.splitSentences(text):
                    translation = tn.translateLanguage(TRANSLATION_KEY,sentence,'auto','en')
                    print(f"Text to be translated: {text}\ntranslated text:{translation}")
            else:
                print(f"Last screengrab was too similar to the current one\n\nTHRESHOLD: {threshold} | DIFF: {diff}")

main()
