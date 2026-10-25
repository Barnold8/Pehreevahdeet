import requests


def detectLanguage(api_key: str,input_text: str)-> :
 
    API_URL = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/detect"

    payload = input_text

    headers = {
	    "x-rapidapi-key" : api_key,
        "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type"   : "text/plain"
    }

    response = requests.post(API_URL, data=payload, headers=headers)
    response = response.json()


    return response.json()

def translate(api_key: str,input_text: str,source: str,target_lang: str)->str:

    API_URL  = "https://multi-format-ai-translator-the-most-complete.p.rapidapi.com/translate"

    querystring = {"source":"auto","target":target}

    payload = input_text

    headers = {
	    "x-rapidapi-key": api_key,  
        "x-rapidapi-host": "multi-format-ai-translator-the-most-complete.p.rapidapi.com",
	    "Content-Type": "text/plain"
    }

    response = requests.post(API_URL)

    print(response.json()) 
    return ""



