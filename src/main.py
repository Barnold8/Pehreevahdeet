try:
    # Needed lib code
    import time
    import json
    from typing import List
    # My own code
    import utils
    import image as img
    import translation as tn

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code. Have you activated the venv?\n\nHave you ran pip install -r requirements.txt while in said venv?\n\nERROR:{MNFE}")

  
def main():
   
    POLL_RATE           = 50
    running             = True
    OCR_KEY             = utils.getAPIKey('API_KEY_OCR')
    TRANSLATION_KEY     = utils.getAPIKey('API_KEY_TRANSLATE')
    
    if __name__ == "__main__":

        monitors = utils.getMonitors()

        while(running):

            sleepInNano(POLL_RATE) # free up cpu usage
            screen      = img.getScreen(monitors[0])
            out         = img.OCR(screen,OCR_KEY)
            text        = getMessage(out)
            
            for sentence in splitSentences(text):
                translation = tn.translateLanguage(TRANSLATION_KEY,sentence,'auto','en')
                print(f"HI: {translation}")

            running = False
            
main()
