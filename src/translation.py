import requests
import API_watchdog as wd
from API_watchdog import Eye
import time
import settings
from utils import errPrint

def translateLanguage(api_key: str,input_text: str,source_lang: str,target_lang: str)->str:

    # check if cooldown, if so, sleep
    wd.Watchdog.attemptSleep(Eye.TRANSLATION) 

    API_URL     = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/translate"
    ERR_MESG    = "Could not translate text. Don't see any errors? Enable show"
    querystring = {"source":source_lang,"target":target_lang}

    payload = input_text 
    headers = {
	    "x-rapidapi-key": api_key , 
	    "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type": "text/plain"
    }
    
    response = requests.post(API_URL, data=payload, headers=headers, params=querystring)
    
    if response.status_code >= 300 or response.status_code < 200 and settings.Dev.SHOW_WARNINGS:
       
        if settings.Dev.DEBUG_WATCHDOG:
            print(f"translateLanguage | Error: Got error code {reponse.status_code}\n\nPayload\n\ninput text: {input_text}\n\nsource_lang: {source_lang}\n\ntarget_lang: {target_lang}")
        if settings.Dev.SHOW_WARNINGS:
            print(f"translateLanguage | Debug: The call to the translation API threw a {response.status_code} status code. Check here for more information https://developer.mozilla.org/en-US/docs/Web/HTTP/Reference/Status")

        wd.Watchdog.closeEye(Eye.TRANSLATION)

        return ERR_MESG
    
    response = response.json()
    
    try:
        response = response['data']['translated_text'] 
    except KeyError as KE:
        print(f"Error: While accessing the response JSON, a key was attempted to be accessed. It's possible the PI responses have changed significantly enough to cause this error.")
        return ERR_MESG

    return response




