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
    print(f"Encountered an error when importing library code.\n\nERROR:{MNFE}")

def sleepInNano(nano_seconds: int)-> None:
    time.sleep(nano_seconds/1000000.0)

def getMessage(unserialised:str) -> List[str]:
    try:
        payload = json.loads(unserialised)["ParsedResults"]
        payload = payload[0]
        payload = payload["ParsedText"]
        return payload.split("\n")
        
    except KeyError as KE:
        errPrint(f"Error: could not read from API output.\n\nFULL ERROR: {KE}")


def splitSentences(sentences: List [str],chunk_amount: int = 100)-> List[str]:
    # This function takes multiple sentences and makes them into one string
    # The intended outcome of this is to avoid rate limiting of the translation API with the caveat of some outputs being weird

    print(type(sentences))
    if len(sentences) <= chunk_amount:
        return ["".join(sentences)]

    counter = 0
    strings = []
    str_buffer = []

    for sentence in sentences:
        if counter >= chunk_amount:
            counter = 0
            new_string = "".join(str_buffer)
            strings.append(str_buffer)
            str_buffer = []
        str_buffer.append(sentence)
        counter += 1

    if len(str_buffer) > 0:
        strings.append("".join[str_buffer])
    return strings
    
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

            running = False
            print(translation)
            


main()
