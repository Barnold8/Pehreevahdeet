import requests
import utils

def detectLanguage(api_key: str,input_text: str) -> str:
 
    API_URL  = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/detect"
    ERR_MESG = "detectfail"
    payload  = input_text

    headers = {
	    "x-rapidapi-key" : api_key,
        "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type"   : "text/plain"
    }

    try:
        response = requests.post(API_URL, data=payload, headers=headers)
        response = response.json()
    except Exception as e:
        errPrint("Error: problem ocurred while contacting the translation API - DETECT")
        return ERR_MESG
    try:
        language = response["data"]
    except KeyError as KE:
        errPrint("Error: problem ocurred while accessing detection response - DETECT")
        return ERR_MESG

    return language

def translateLanguage(api_key: str,input_text: str,source_lang: str,target_lang: str)->str:

    url = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/translate"

    querystring = {"source":source_lang,"target":target_lang}

    payload = "ik ben een meisje" 
    headers = {
	    "x-rapidapi-key": api_key , 
	    "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type": "text/plain"
    }

    try:
        response = requests.post(API_URL, data=payload, headers=headers)
        response = response.json()
    except Exception as e:
        errPrint("Error: problem ocurred while contacting the translation API - TRANSLATE")
        return ERR_MESG
    try:
        language = response["data"]["translated_text"]
    except KeyError as KE:
        errPrint("Error: problem ocurred while accessing detection response - TRANSLATE")
        return ERR_MESG

    return language
