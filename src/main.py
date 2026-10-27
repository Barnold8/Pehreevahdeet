try:
    import utils
    import image as img
    import translation as tn
    import settings
    from PIL import Image

except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code. Have you activated the venv?\n\nHave you ran pip install -r requirements.txt while in said venv?\n\nERROR:{MNFE}")
 
def main():

    settings.loadConfig("config.json")
    if settings.Dev.SHOW_SETTINGS:
        settings.printSettings()

    POLL_RATE           = settings.System.POLL_RATE
    threshold           = settings.Image.THRESHOLD
    OCR_KEY             = utils.getAPIKey('API_KEY_OCR')
    TRANSLATION_KEY     = utils.getAPIKey('API_KEY_TRANSLATE')
    prev_img            = None
    running             = True

       if __name__ == "__main__":

        monitors = utils.getMonitors()

        while(settings.Dev.RUN_COUNT > 0):
            
            if settings.Dev.LIMITED_RUN:
                settings.Dev.RUN_COUNT -= 1

            utils.sleepInNano(POLL_RATE) # free up cpu usage
            screen      = img.getScreen(monitors[0]) # TODO: add way to import user config here with proper error handling
            diff        = img.getImageDiff(screen,prev_img) if prev_img != None else 0  

            if prev_img == None or diff > threshold:
                
                prev_img    = screen
                out         = img.OCR(screen,OCR_KEY)
                text        = img.getMessage(out)
                
                for sentence in utils.splitSentences(text):
                    if Dev.Language.DEBUG_LANGUGE:
                        print(f"Text to be translated: {text}\n"
                    
                    translation = tn.translateLanguage(TRANSLATION_KEY,sentence,'auto','en')
                    print(f"translated text:{translation}")
            else:
                print(f"Last screengrab was too similar to the current one\n\nTHRESHOLD: {threshold} | DIFF: {diff}")

main()
