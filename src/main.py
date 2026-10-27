try:
    import utils
    import image as img
    import translation as tn
    import settings
    import API_watchdog as wd
    from PIL import Image
    
except ModuleNotFoundError as MNFE:
    print(f"Encountered an error when importing library code. Have you activated the venv?\n\nHave you ran pip install -r requirements.txt while in said venv?\n\nERROR:{MNFE}")

def main():

    settings.loadConfig(".config/config.json")
    
    if settings.Dev.SHOW_SETTINGS:
        settings.printSettings()

    POLL_RATE           = settings.System.POLL_RATE
    threshold           = settings.Image.THRESHOLD
    OCR_KEY             = utils.getAPIKey('.config/API_KEY_OCR')
    TRANSLATION_KEY     = utils.getAPIKey('.config/API_KEY_TRANSLATE')
    monitors            = utils.getMonitors()
    monitor_index       = img.safeGuardMonitorIndex(monitors,settings.Screen.MONITOR_INDEX)
    prev_img            = None
    running             = True
    run_ocr             = True

    if __name__ == "__main__": 

        while(settings.Dev.RUN_COUNT > 0):

            utils.sleepInNano(POLL_RATE) # free up cpu usage
            if settings.Dev.LIMITED_RUN:
                settings.Dev.RUN_COUNT -= 1

            screen      = img.getScreen(monitors[monitor_index]) 
            diff        = img.getImageDiff(screen,prev_img) if prev_img != None else 0.0  

            if prev_img == None or diff > threshold:
                
                prev_img    = screen
                if wd.Watchdog.ocr == False:
                    out         = img.OCR(screen,OCR_KEY)
                    text        = img.getMessage(out)
                    sentences   = utils.splitSentences(text)
                    for sentence in sentences:
                        if settings.Dev.DEBUG_LANGUAGE:
                            print(f"DEBUG: Text to be translated: {text}\n\nText split into sentences {sentences}")
                            print(f"DEBUG: Payload to be sent to translateLanguage function\n\nsentence:{type(sentence)}\n\nsource_lang:'auto'\n\ntarget_lang: {settings.Language.TARGET_LANGUAGE}") 
                        translation = tn.translateLanguage(TRANSLATION_KEY,sentence,'auto',settings.Language.TARGET_LANGUAGE)
                        print(f"translated text: {translation}")
                else:
                    if settings.Dev.DEBUG_LANGUAGE:
                        print(f"Last screengrab was too similar to the current one\n\nTHRESHOLD: {threshold} | DIFF: {diff}")

main()
