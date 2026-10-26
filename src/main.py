try:
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

            utils.sleepInNano(POLL_RATE) # free up cpu usage
            screen      = img.getScreen(monitors[0])
            out         = img.OCR(screen,OCR_KEY)
            text        = img.getMessage(out)
            
            for sentence in utils.splitSentences(text):
                translation = tn.translateLanguage(TRANSLATION_KEY,sentence,'auto','en')
                print(f"Text to be translated: {text}\ntranslated text:{translation}")

                        
main()
