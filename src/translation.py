import requests


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
        print("Error: problem ocurred while contacting the translation API - DETECT")
        return ERR_MESG
    try:
        language = response["data"]
    except KeyError as KE:
        print("Error: problem ocurred while accessing detection response - DETECT")
        return ERR_MESG

    return language

def translateLanguage(api_key: str,input_text: str,source: str,target_lang: str)->str:

    API_URL  = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/translate"

    querystring = {"source":"auto","target":target}

    payload = input_text

    headers = {
	    "x-rapidapi-key": api_key,  
        "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type": "text/plain"
    }

    response = requests.post(API_URL)
    response.json() 


    return ""



