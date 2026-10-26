import sys
import screeninfo
import time

def sleepInNano(nano_seconds: int)-> None:
    time.sleep(nano_seconds/1000000.0)
 
def getMonitors():
    return screeninfo.get_monitors()

def errPrint(*args:str, **kwargs:str)->None:
    print(*args, file=sys.stderr, **kwargs)

def getAPIKey(path:str)->str:

    try:
        with open(path,'r') as file:
            try:
                key =  file.readlines()[0]
                return  ''.join(key.split())
            except IndexError:
                errPrint(f"Error: {path} is either empty or corrupt")
    except FileNotFoundError as FNFE:
        errPrint(f"Error: {path} does not exist")

def splitSentences(sentences: List [str],chunk_amount: int = 100)-> List[str]:
    # This function takes multiple sentences and makes them into one string
    # The intended outcome of this is to avoid rate limiting of the translation API with the caveat of some outputs being weird

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
 
