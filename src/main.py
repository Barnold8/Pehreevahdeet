try:
    # Needed lib code
    import time
    import json
    from typing import List
    # My own code
    import utils
    import image as img

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

    
def main():
   
    POLL_RATE = 50
    running   = True
    KEY = utils.getAPIKey('API_KEY')

    if __name__ == "__main__":

        monitors = utils.getMonitors()

        while(running):

            sleepInNano(POLL_RATE) # free up cpu usage
            screen = img.getScreen(monitors[0])
            out = img.OCR(screen,KEY)
            running = False
            text = getMessage(out)      


        print(text)

main()
