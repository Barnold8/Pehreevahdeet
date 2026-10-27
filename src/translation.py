import requests
import API_watchdog
import time
import settings
from utils import errPrint

def translateLanguage(api_key: str,input_text: str,source_lang: str,target_lang: str)->str:

    if API_watchdog.translation:
        time.sleep(settings.System.API_COOLDOWN)
        API_watchdog.translation = False

    API_URL     = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/translate"
    ERR_MESG    = "translatefail"
    querystring = {"source":source_lang,"target":target_lang}

    payload = input_text 
    headers = {
	    "x-rapidapi-key": api_key , 
	    "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type": "text/plain"
    }
    
    response = requests.post(API_URL, data=payload, headers=headers, params=querystring)
    if response.status_code >= 300 or response.status_code < 200 and settings.Dev.SHOW_WARNINGS:
        print(f"Error: The call to the translation API threw a {response.status_code} status code. Check here for more information https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status")
        return ERR_MESG
    response = response.json()
    
    try:
        response = response['data']['translated_text'] 
    except KeyError as KE:
        API_watchdog.translation = True
        print(f"Error: While accessing the response JSON, a key was attempted to be accessed. It's possible the PI responses have changed significantly enough to cause this error.")
        return ERR_MESG

    return response




