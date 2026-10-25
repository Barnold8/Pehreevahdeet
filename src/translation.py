import requests
from utils import errPrint

# note: mostly duplicated code and error handling could be done with an Enum but oh well

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
        errPrint(f"Error: problem ocurred while contacting the translation API - DETECT\n\n{KE}")
        return ERR_MESG
    try:
        language = response["data"]
    except KeyError as KE:
        errPrint(f"Error: problem ocurred while accessing detection response - DETECT\n\n{KE}")
        return ERR_MESG

    return language

def translateLanguage(api_key: str,input_text: str,source_lang: str,target_lang: str)->str:

    API_URL     = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/translate"
    ERR_MESG    = "translatefail"
    querystring = {"source":source_lang,"target":target_lang}

    payload = input_text 
    headers = {
	    "x-rapidapi-key": api_key , 
	    "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type": "text/plain"
    }
    
    try:
        response = requests.post(API_URL, data=payload, headers=headers, params=querystring)
        response = response.json()
        response = response['data']['translated_text'] 
    except Exception as e:
        print("Error: problem ocurred while sending text off to be translated - TRANSLATION")

    return response




